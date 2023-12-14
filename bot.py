import os
os.environ["OPENAI_API_KEY"] = "paste your api key"
urls =["https://coal.nic.in/acts-rules-policies"]
from langchain.document_loaders import UnstructuredURLLoader
loaders = UnstructuredURLLoader(urls)
data = loaders.load()
data
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(separator='\n',chunk_size=1000,chunk_overlap=200)
docs = text_splitter.split_documents(data)
docs
import pickle
import faiss
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
embeddings
vectorstore_OpenAI = FAISS.from_documents(docs,embeddings)
vectorstore_OpenAI.save_local("faiss_store")
#Assign this to a variable
kal =FAISS.load_local("faiss_store", OpenAIEmbeddings())
kal
llm=OpenAI(temperature=0, model_name='text-davinci-003')
llm
chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=kal.as_retriever())
chain({"question": "What is mining?"}, return_only_outputs=True)



