from langchain_openai import OpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType

llm = OpenAI(temperature=0, model="gpt-3.5-turbo-instruct")
tools= load_tools(["human"])

agent_chain = initialize_agent(llm=llm, tools=tools, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent_chain.run("What is Lino's Last Name?")