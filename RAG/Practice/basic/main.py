from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
load_dotenv()
import os 


model=ChatMistralAI(model="mistral-small-2506")

result=model.invoke("what is RAG?")
print(result.content)