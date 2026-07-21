from langchain_community.document_loaders import PyPDFLoader
from langchain_mistralai import MistralAIEmbeddings, ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langch  

import json
from dotenv import load_dotenv
load_dotenv()
llm = ChatMistralAI(model="mistral-small-latest")
loader=PyPDFLoader("resume.pdf")
docs=loader.load()
context=[]
for doc in docs:
    context.append(doc.page_content)
with open("data.json","w") as f:
    json.dump(context,f,indent=4)

prompttemplate=ChatPromptTemplate.from_messages([("system","assume you are a recruiter who needs to analyze the resume information extract needed information from resume context which is given context   "),("human",'''Context:{context},Question:{question} ''')])


question="find the technical skills section dont anaylze of make chnages whatever technical skills mentioned in technical skills section of context only give that , strict mandatory : only give technical skills section , dont make them understand or make them analyze "



# final_prompt=prompttemplate.invoke({"context":context,"question":question})
# response=llm.invoke(final_prompt)

# print(response.content)


