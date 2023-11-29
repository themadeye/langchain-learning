# Get Started

To run and play with this demo, make sure you set up your environment correctly(make sure you have Python version 3.11 or higher, as long as the python package manager `pip`/`pip3` installed).

**Install packages**

Globally:

`pip3 install -r requirements.txt`

With Python virtual environment:
1. Navigate to the project folder
2. Create a new virtual environment in that folder:\
`python3 -m venv .venv` \
When you run the command above, a directory called .venv will appear in the folder. This directory is where your virtual environment and its dependencies are installed.
3. Navigate into the `.venv/bin` folder and activate your virtual environment:\
`source bin/activate`
4. Now you can install the neccessary packages, navigate back to the project root dir and then run:\
`pip3 install -r requirements.txt`

5. To deactivate your current virtual environment, simply run:\
`deactivate`\
> :warning: **Don't deactivate the environment when you are developing or running the project**!

**Try out the demo**

1. replace your Open AI API key in the `.env` file.
2. And simply run:\
`streamlit run ./src/main/main.py`

You can find the example text file in the folder `./txtsample` to test the demo, or you can upload your own .txt file(it can be an article, a news, essay, etc)

# What is this demo?
This app is a demostration of creating a simple question-answering application using LangChain. Upload any .txt file and ask a questions regards to that file, it will analyze the document and generate an answer.

It takes the uploaded .txt document, splitting it into a chunks of string, turn it into vector embeddings and store into the vector database(ChromaDB in this case). With the index and the vector stored in place, we can now use RetrievalQA from LangChain to generate an answer:

1. Accept the user's question
2. Analyze and identify the relavant content from the document based on the given questions
2. Pass the questions and the document's content as a prompt into the LLM(chat gpt in this case) and generate an answer.

The idea of this demo is to practice the learning of LangChain Retrieval-augmented generation(RAG) use case:\
https://python.langchain.com/docs/use_cases/question_answering/#step-4-retrieve

the concept is to be able to consumes some given input(.txt file, raw string data, formatted data, etc), store it as vector data, retrieve it and analyze with some requirements(questions, etc) and generate output.
