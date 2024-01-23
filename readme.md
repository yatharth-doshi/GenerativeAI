# Github GenAI

The Github GenAI is used to fetch the repository information and its contents to produce generative response based on the question asked about it. It uses the concept of GenerativeAI to give answers to the question.

## Key features:
1. Github Repository Information Retrieval
▪ Users can input a github repository URL and select their knowledge level. The
application fetches essential repository details using the github API, including the repository name, programming languages utilized, and information about the repository owner. This provides users with a quick overview of a github project
2. Content Summarization
▪ For users with a basic knowledge level, the application reads the README.md
file of the specified repository. It then generates a concise summary of the project’s purpose that helps the users to understand the repository’s content.
3. Code Entity Search
▪ The users that are completely familiar with the repository can ask specific
questions related to code entities. The application clones the repository locally, searches for relevant code snippets, and provides information based on the mention code entities.

## System requirements:
• System with python 3 or Higher installed
• Minimum 16 GB of RAM
• 20 GB free disk space required

## Installation and execution instructions:
1. Download ZIP file from the URL:
2. Extract the ZIP file on your device
3. Open directory in any IDE

4. Install the requirements.txt file to get the dependencies required to run the code using pip install -r requirements.txt
5. Run the app.py file using: python app.py
 
6. Open the URL http://127.0.0.1:5000 in any browser

## Usage Instruction:
1. After completing the previous steps when you open this URL: http://127.0.0.1:5000 
  1. Enter the github URL. Ie: https://github.com/Alathrop2/Python-QuickSort
  2. Select Knowledge Level based on your understand to the repository. ie: Completely familiar
  3. Enter question. ie: how quick_sort algorithm is implemented
  4. Click on “Generate Response” Button 
  5. Wait for the result to be generated
2. This response is generated from repository to explain function quick_sort() used 

## Limitations:
1. If the prompt is wrong then the model might generate inaccurate results.
2. It does not support the text of more than 2048 tokens.
3. It might take some time to generate response since the repo is first cloned to the device and then searched for the entities.
4. To make the execution time faster and efficient it requires the use of GPU and more RAM size.
5. The code returns the first entry of the keyword entity and not search for other occurrences which may be more relevant.
