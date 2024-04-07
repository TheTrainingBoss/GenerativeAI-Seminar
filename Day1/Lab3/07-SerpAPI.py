from langchain_openai import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain.chains import LLMMathChain
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain.agents.tools import Tool

llm = OpenAI(temperature=0, model="gpt-3.5-turbo-instruct") 
prompt = "Where is the upcoming Summer Olympics going to take place? and what is the population of that country raised to the 0.43 power?"
llm_math_chain = LLMMathChain.from_llm(llm, verbose=True)   
search = SerpAPIWrapper()
wikipedia = WikipediaAPIWrapper()

tools = [
    Tool(
        name="Search", 
        func=search.run,
        description="Searches the web for the answer to a question on current events"
        ),
    Tool(
        name="Wikipedia", 
        func=wikipedia.run,
        description = "Searches Wikipedia for the answer to a question looking up facts and statistics"
        ), 
    Tool(
        name="Calculator", 
        func=llm_math_chain.run,
        description = "Performs mathematical calculations"
        )
    ]

model = ChatOpenAI(temperature=0)
planner = load_chat_planner(model)
executor = load_agent_executor(model, tools, verbose=True)

agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

agent.invoke(prompt)
