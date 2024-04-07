from langchain_openai import OpenAI

# https://platform.openai.com/docs/deprecations
llm = OpenAI(temperature=0.9)
prompt = "What is a good name for a workshop on Generative AI at a technical conference in Las Vegas?"


result = llm.generate([prompt]*5)
for session_name in result.generations:
    print(session_name[0].text)