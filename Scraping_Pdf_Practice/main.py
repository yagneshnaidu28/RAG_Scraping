from pdfminer.high_level import extract_pages,extract_text
import re

requirement=["html","css","js","python","fastapi"]
text=extract_text("yagnesh_resume_tops.pdf")
# print(text)

for i in text:
    for j in requirement:
        if i==j:
            print("found our requirements here at :",i)


""" information=[]

for page_layout in extract_pages("yagnesh_resume_tops.pdf"):
    for element in page_layout:
        information.append(element)

print(information[4]) """