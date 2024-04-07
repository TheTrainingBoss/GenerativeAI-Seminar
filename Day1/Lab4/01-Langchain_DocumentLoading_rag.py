from langchain_openai import OpenAI
#from langchain_community.document_loaders import TextLoader
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import chroma
from langchain.chains import RetrievalQA

pdfreader = PdfReader('./sotu2023.pdf')
#loader = TextLoader('sotu2023.txt')

from typing_extensions import Concatenate
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

#documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_text(raw_text)

#print(texts[0])

embeddings = OpenAIEmbeddings()
store = chroma.Chroma.from_texts(texts, embeddings, collection_name="sotu2023")

llm = OpenAI(temperature=0.9)
chain = RetrievalQA.from_chain_type(llm, retriever=store.as_retriever(), verbose=True)

print(chain.invoke("What did the president say about medicine?"))