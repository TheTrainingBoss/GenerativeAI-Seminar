from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

template = "You are a Software Architect. What is a good name for a workshop on {technology} at a Technical conference?"

prompt = PromptTemplate.from_template(template)

llm = OpenAI(temperature=0.9, model="gpt-3.5-turbo-instruct")

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.invoke("Generative AI"))