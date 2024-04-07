from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain

template = "You are a Software Architect. What is a good name for a workshop on {technology} at a Technical conference?"

llm = OpenAI(temperature=0.9, model="gpt-3.5-turbo-instruct")

first_prompt = PromptTemplate.from_template(template)
first_chain = LLMChain(llm=llm, prompt=first_prompt)

second_template = "Write a catchy slogan for the {workshop}"
second_prompt = PromptTemplate.from_template(second_template)
second_chain = LLMChain(llm=llm, prompt=second_prompt)

OverallChain = SimpleSequentialChain(chains=[first_chain, second_chain], verbose=True)

catchphrase = OverallChain.invoke("Generative AI") 
print(catchphrase)