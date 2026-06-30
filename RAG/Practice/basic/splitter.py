""" CharacterTextSplitter """
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain_text_splitters import CharacterTextSplitter,TokenTextSplitter
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
data=PyPDFLoader(r"C:\Users\LENOVO\Downloads\All_Practices\RAG_Scraping\RAG\Langchain_RAG_Concepts\document loaders\GRU.pdf")
docs=data.load()
splitter=TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=1,
)
chunks=splitter.split_documents(docs)
print(chunks[100].page_content)

