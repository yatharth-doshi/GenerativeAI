from repo_info import fetch_repo_languages, calculate_language_percentages
from search_from_repo import clone_and_search_repo

# Generate a response based on the knowledge level and user's question.
def generate_response(knowledge_level, repo_info, question):
    
    # This knowledge level fetches the repo info and shows the details of the repo
    if knowledge_level == "None":
        languages_data = fetch_repo_languages(repo_info['owner']['login'], repo_info['name'])
        languages_info = "\n".join([f"- {lang}: {percentage:.2f}%" for lang, percentage in calculate_language_percentages(languages_data).items()])
        return f'''The name of the Repo is: {repo_info['name']}, the programming language(s) used in this repo are:\n{languages_info} and Repo is Developed by {repo_info['owner']['login']}, {repo_info['description']}. "just display this info with the exact sentence provided"'''

    # This knowledge level reads the README.md to understand the project details and explains it
    elif knowledge_level == "Basic":
        keywords = question
        search_result = clone_and_search_repo(repo_info['url'], keywords, 'Basic')
        return f"my repository name is {repo_info['name']} and its details are: {search_result} please explain in brief what does this repository do."

    # This knowledge level can find the code entities present in the repo and explain it
    elif knowledge_level == "Completely Familiar":
        original_ques = question
        keywords = question.split()
        search_result = clone_and_search_repo(repo_info['url'], keywords)
        search_result = f'''explain {original_ques} in the following code snippet:\n{search_result}? with relevant code.'''
        return search_result

    return "Invalid knowledge level."