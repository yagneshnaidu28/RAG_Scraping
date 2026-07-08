import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from langchain_community.retrievers import ArxivRetriever

retriever=ArxivRetriever(
    load_max_docs=2,      #number of papers to retrieve
    load_all_available_meta=True
)

# query retriever
docs=retriever.invoke("large language models")


# print results
for i ,doc in enumerate(docs):
    print(f"\n Result{i+1}")
    print("Title:",doc.metadata.get("Title"))
    print("Authors:",doc.metadata.get("Authors"))
    print("summary:",doc.page_content[:500])