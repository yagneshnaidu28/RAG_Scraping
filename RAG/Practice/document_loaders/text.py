from langchain_community.document_loaders import TextLoader

data=TextLoader("notes.txt")

print(data.load()[0].page_content)

# print(data.load().page_content)