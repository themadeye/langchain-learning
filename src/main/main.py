__import__('pysqlite3')
import os
import streamlit as st
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

load_dotenv() # read local .env file
api_key = os.getenv('OPENAI_API_KEY')

def generate_response(uploaded_file, api_key, prompt_text):
      # Load the document once the file is uploaded
      if uploaded_file is not None:
            documents = [uploaded_file.read().decode()]
      # Split the loaded documents into chunks
      text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
      texts = text_splitter.create_documents(documents)
      # Select embeddings
      embeddings = OpenAIEmbeddings(openai_api_key=api_key)
      # Create a vectorstore from documents
      db = Chroma.from_documents(texts, embeddings)
      # Create retriever interface
      retriever = db.as_retriever()
      # Create QA chain
      qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=api_key), chain_type='stuff', retriever=retriever)
      return qa.run(prompt_text)

# Page title using Streamlit, by doing this, we get rid of the need of writting frontend code.
st.set_page_config(page_title='🦜🔗 Ask me')
st.title('🦜🔗 Ask me')

# Next, add the neccessary front end widgets: File upload and text field components.
uploaded_file = st.file_uploader('Upload an article', type='txt')
prompt_text = st.text_input("What's on your mind?:", placeholder = '', disabled=not uploaded_file)

# Form input and query
result = []
with st.form('myform', clear_on_submit=True):
      submitted = st.form_submit_button('Submit', disabled=not(uploaded_file and prompt_text))
      if submitted:
            with st.spinner('We are working hard on it...'):
                  response = generate_response(uploaded_file, api_key, prompt_text)
                  result.append(response)
      
      if len(result):
            st.info(response)