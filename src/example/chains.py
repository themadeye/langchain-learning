import os
import openai
import datetime
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

load_dotenv() # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')
current_date = datetime.datetime.now().date()
target_date = datetime.date(2024, 6, 12)

if current_date > target_date:
    llm_model = "gpt-3.5-turbo"
else:
    llm_model = "gpt-3.5-turbo-0301"

llm = ChatOpenAI(temperature=0.0, model=llm_model) 

# This is the overall chain where we run these two chains in sequence.
from langchain.chains import SimpleSequentialChain

def sequance_chain():
      first_prompt = ChatPromptTemplate.from_template("What is the best name to describe \a company that makes {product}?")
      chain_one = LLMChain(llm=llm, prompt=first_prompt)

      second_prompt = ChatPromptTemplate.from_template("Write a 20 words description for the following \company:{company_name}")
      chain_two = LLMChain(llm=llm, prompt=second_prompt)

      overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two], verbose=True)
      answer = overall_simple_chain.run("Smartphone")
      print(answer)

sequance_chain()