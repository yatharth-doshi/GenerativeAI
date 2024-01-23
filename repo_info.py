from urllib.parse import urlparse
import requests

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com/repos/"

# Check the validity of a GitHub repository URL and extract owner and repo details.
def repository_url_check(repo_url):
    
    try:
        # Parse the GitHub URL
        parsed_url = urlparse(repo_url)

        # Check if it's a valid GitHub repository URL
        if not (parsed_url.netloc == "github.com" and len(parsed_url.path.rstrip('/').split('/')) >= 3):
            return "Invalid GitHub repository URL"

        # Extract owner and repo from the parsed URL
        path_parts = parsed_url.path.rstrip('/').split('/')
        owner = path_parts[1]
        repo = path_parts[2].replace('.git', '')

        return owner, repo

    except ValueError:
        return "Invalid GitHub repository URL"
    except requests.RequestException as e:
        return f"Error getting Repo {str(e)}"

# Fetch repository information from the GitHub API.
def fetch_repo_info(owner, repo_name):
    
    api_url = f"{GITHUB_API_URL}{owner}/{repo_name}"
    headers = {"Authorization": "Token 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"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    return None

# Fetch language information for a repository from the GitHub API.
def fetch_repo_languages(owner, repo_name):
    
    api_url = f"{GITHUB_API_URL}{owner}/{repo_name}/languages"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    return None

# Calculate the percentage of lines of code for each programming language.
def calculate_language_percentages(languages_data):

    total_lines_of_code = sum(languages_data.values())
    language_percentages = {lang: (lines / total_lines_of_code) * 100 for lang, lines in languages_data.items()}
    return language_percentages