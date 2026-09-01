
# this is basic coding of extracting data from documents and storing them to database using basic search like similarity search and retriever we are retrieving data


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

""" 
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_core.documents import Document
load_dotenv()

docs=[
    Document(page_content="python is widely used in artificial intelligence",metadata={"source":"AI_book"}),
    Document(page_content="pandas is used for data analysis in python ",metadata={"source":"DataScience_book"}),
    Document(page_content="neural networks are used in deep learning",metadata={"source":"DL_book"}),
]

embedding_model=MistralAIEmbeddings()

vectorstore =Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma-db",
)

result=vectorstore.similarity_search("what is neural network?")
# print(result)
print("---------------------------------------------------------------------------")
for r in result:
    print(r.page_content)
    break


print("---------------------------------------------------------------------------")

retriver = vectorstore.as_retriever()

docs = retriver.invoke("Explain deep learning")

print(docs) """










# this program is exact which we needed:

""" load pdf
split into chunks 
create embeddings
store it to chroma """

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma

from dotenv import load_dotenv
load_dotenv()

loader=PyPDFLoader("../document_loaders/GRU.pdf")
docs=loader.load()
# print(docs)


splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(docs)


vectorstore =Chroma.from_documents(
    documents=chunks,
    embedding=MistralAIEmbeddings(),
    persist_directory="chroma_db"
)


