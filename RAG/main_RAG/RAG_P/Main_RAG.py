from langchain_mistralai import MistralAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader("resume.pdf")
docs=loader.load()
for doc in docs:
    print(doc.page_content)