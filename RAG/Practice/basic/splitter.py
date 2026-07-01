""" CharacterTextSplitter """
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain_text_splitters import CharacterTextSplitter,TokenTextSplitter,RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader,PyPDFLoader


""" 

splitter=CharacterTextSplitter(
    separator="",
    chunk_size=20,
    chunk_overlap=1
)

data=TextLoader("../document_loaders/notes.txt")

docs=data.load()
chunks=splitter.split_documents(docs)
for i in chunks:
    print(i.page_content)
 """


""" Token-based Splitting """
# data=PyPDFLoader("../document_loaders/GRU.pdf")
""" docs=data.load()
splitter=TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=1,
)
chunks=splitter.split_documents(docs)
print(chunks[100].page_content) """




""" Meaning/semantic-Based Splitting(RecursiveCharacterTextSplitter) """


loader=PyPDFLoader("../document_loaders/GRU.pdf")
docs=loader.load()
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
texts=text_splitter.split_documents(docs)
print(texts[0].page_content)
print(texts[10].page_content)