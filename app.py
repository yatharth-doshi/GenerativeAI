from flask import Flask, render_template, request
from repo_info import fetch_repo_info, repository_url_check
from model import gen_ai
import json

app = Flask(__name__)

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

# AJAX rendering is used in this route
@app.route('/generate', methods=['POST'])
def generate():

    # Handle the form submission
    repo_url = request.form['repo_url']
    knowledge_level = request.form['knowledge_level']
    question = request.form['question']

    # Extract owner and repo name from the repository URL
    owner, repo_name = repository_url_check(repo_url)

    # Fetch repository information, languages, and contents
    repo_info = fetch_repo_info(owner, repo_name)
    # repo_content = fetch_repo_contents(owner, repo_name)

    if repo_info:
        
        answer = gen_ai(knowledge_level, repo_info, question)

        result_dict = {"answer": answer, "repo_url": repo_url, "knowledge_level": knowledge_level, "question": question}
        json_result = json.dumps(result_dict, indent=2)
        return json_result

    return "Unable to fetch repository information. Please check the URL or try again later."

if __name__ == '__main__':
    app.run(debug=True)
