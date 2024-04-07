from langchain_openai import OpenAI
from langchain.agents import get_all_tool_names, load_tools, initialize_agent
import pprint

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(get_all_tool_names())

llm = OpenAI(temperature=0, model="gpt-3.5-turbo-instruct")
tools = load_tools(llm=llm, tool_names=["wikipedia", "llm-math"])

agent = initialize_agent(llm=llm, tools=tools, agent="zero-shot-react-description", verbose=True)

prompt = "What year Bill Gates was born? and what is that year raised to the power of 3?"

agent.invoke(prompt)