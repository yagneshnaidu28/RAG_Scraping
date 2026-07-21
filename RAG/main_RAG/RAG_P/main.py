from langchain_mistralai import MistralAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader("resume.pdf")
context=[]
docs=loader.load()
for doc in docs:
    context.append(doc.page_content)

print(context)
    