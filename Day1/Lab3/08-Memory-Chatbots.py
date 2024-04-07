from langchain_openai import OpenAI
from langchain.chains import ConversationChain

llm = OpenAI(temperature=0, model="gpt-3.5-turbo-instruct")
conversation = ConversationChain(llm=llm, verbose=True)

#print(conversation.predict(input="Hi There!"))

print("Welcome to the TTB Chatbot! What's on your mind?")

for _ in range(0,3):
    human_input = input("You: ")
    ai_response = conversation.predict(input=human_input)
    print(f"AI: {ai_response}")