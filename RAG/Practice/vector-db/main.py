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

for d in docs:
    print(d.page_content)
    break