from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
output_parser = StrOutputParser()

#Notice the syntax for LCEL with the pipe operator | to chain the components
chain = prompt | model | output_parser

print(chain.invoke({"topic": "ice cream"}))