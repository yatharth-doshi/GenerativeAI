from urllib.parse import urlparse
from nltk.corpus import stopwords
import re
import requests
import os

# Clone the repo on local device and search for code entities
def clone_and_search_repo(repo_url, keywords, file_name=''):

    # Extract repository name from URL
    repo_name = os.path.splitext(os.path.basename(urlparse(repo_url).path))[0]

    # Check if the local repository already exists
    local_repo_path = 'local_repo'
    repo_path = os.path.join(local_repo_path, repo_name)

    if not os.path.exists(repo_path):
        # Clone the repository locally
        clone_url = requests.get(repo_url).json()['clone_url']
        os.makedirs(repo_path, exist_ok=True)
        os.system(f'git clone {clone_url} {repo_path}')

    # Search through the local repository
    result = search_repo_local(repo_path, keywords, file_name)

    return result

# Implementation of searching code entities
def search_repo_local(local_path, keywords, file_name=''):
    stop_words = set(stopwords.words('english'))

    for root, dirs, files in os.walk(local_path):
        # Exclude specific folders like .git and images
        dirs[:] = [d for d in dirs if d not in ['.git', 'images']]

        for file in files:
            file_path = os.path.join(root, file)

            if file_name == 'Basic' and file.endswith('README.md'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    return file_content

            if not file.endswith('README.md') and not file.endswith('.json'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                except UnicodeDecodeError:
                    # If decoding as utf-8 fails, try a different encoding or skip the file
                    continue

                # Remove stop words from the keywords
                filtered_keywords = [word for keyword in keywords for word in re.split(r'\W+', keyword) if word.lower() not in stop_words]

                # print(f"Filtered Keywords: {filtered_keywords}")

                # Search through the file content
                for line_num, line in enumerate(file_content.splitlines()):
                    if any(re.search(fr'\b{keyword}\b', line, re.IGNORECASE) for keyword in filtered_keywords):
                        start_line = max(0, line_num)
                        end_line = min(len(file_content), line_num + 50)
                        context_lines = file_content.splitlines()[start_line:end_line]
                        context = "\n".join(context_lines)

                        return context

    return "Code entities not found"