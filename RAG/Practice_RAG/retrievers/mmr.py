import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_mistralai import MistralAIEmbeddings

# Load environmental variables (contains MISTRAL_API_KEY)
load_dotenv()

docs = [
    Document(page_content="Gradient descent is an optimization algorithm used in machine learning."),
    Document(page_content="Gradient descent minimizes the loss function."),
    Document(page_content="Gradient descent  is an optimization that minimizes the loss function."),
    Document(page_content="Neural networks use gradient descent for training."),
    Document(page_content="Support Vector Machines are supervised learning algorithms.")
]

# Use MistralAIEmbeddings which doesn't require local transformers/downloads
embeddings = MistralAIEmbeddings()

vectorstore = Chroma.from_documents(docs, embeddings)

similarity_retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

print("=================similarity search==================")

similarity_docs = similarity_retriever.invoke("what is gradient descent?")
for doc in similarity_docs:
    print(doc.page_content)




print("=================MMR(Max Marginal Relevance)search================")
mmr_retriever=vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k":2}
)
mmr_docs=mmr_retriever.invoke("what is gradient descent")

# for docs in mmr_docs:
#     print(docs.page_content)



print("=================context of retriever================")

context="\n\n".join([d.page_content for d in docs])

print(context)