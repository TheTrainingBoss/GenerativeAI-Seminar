from langchain_openai import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain.schema import messages_from_dict, messages_to_dict

history = ChatMessageHistory()
history.add_user_message("I want to talk about Donkeys")
history.add_ai_message("Let's talk about Donkeys, they are interesting animals.")

dicts = messages_to_dict(history.messages)
print(dicts)

new_mesasges = messages_from_dict(dicts)

llm = OpenAI(temperature=0, model="gpt-3.5-turbo-instruct")
history = ChatMessageHistory(messages=new_mesasges)

buffer = ConversationBufferMemory(chat_memory=history)
conversation = ConversationChain(llm=llm, memory=buffer, verbose=True)  

print(conversation.predict(input="What are they?"))
print(conversation.memory)