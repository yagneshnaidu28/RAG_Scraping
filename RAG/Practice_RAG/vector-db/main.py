import os
from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from  langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Resolve path to chroma_db relative to the script location
current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "chroma_db")

embedding=MistralAIEmbeddings()
vectorstore=Chroma(
    persist_directory=db_dir,
    embedding_function=embedding
)

retriever=vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":4,
        "fetch_k":10,
        "lambda_mult":0.5
    }
)

llm = ChatMistralAI(model="mistral-small-latest")



#prompt template 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","""You are a helpful AI assistant.Use ONLY the provided context to answer the question.If the answer is not present in the context,say: "I could not find the answer in the document."""),
        ("human",
        """Context:{context}
        Question:{question}""")
    ]
)

print("Rag system created ")

print("press 0 to exit ")

while True:
    query = input("You : ")
    if query == "0":
        break 
    
    docs = retriever.invoke(query)
    # print(f"[System: Retrieved {len(docs)} document chunks]")
    for d in docs:
        print(d.page_content)
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    
    final_prompt = prompt.invoke({
        "context" :context,
        "question": query
    })
    
    response = llm.invoke(final_prompt)

    print(f"\n AI: {response.content}")
    