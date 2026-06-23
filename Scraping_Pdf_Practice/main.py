from pdfminer.high_level import extract_pages,extract_text
import re



''''pdfminer library'''
information=[]

for page_layout in extract_pages("yagnesh_resume_tops.pdf"):
    for element in page_layout:
        information.append(element)

print(information[4])

'''Pyreader library'''


from pypdf import PdfReader
reader=PdfReader("yagnesh_resume_tops.pdf")
print(len(reader.pages))
print(reader.pages[1].extract_text())
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(reader.pages[1].extract_text().upper())
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")



'''PdfPlumber'''
import pdfplumber

with pdfplumber.open('yagnesh_resume_tops.pdf') as pdf:
    # iterate over each page
    for page in pdf.pages:
        # extract text
        text = page.extract_text()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<--------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(text)


'''PyMuPdf'''



# The import name for this library is fitz
import fitz

# Create a document object
doc = fitz.open('yagnesh_resume_tops.pdf')  # or fitz.Document(filename)

# Extract the number of pages (int)
print(doc.page_count)

# the metadata (dict) e.g., the author,...
print(doc.metadata)

# Get the page by their index
page = doc.load_page(0)
 # or page = doc[0]

# read a Page
text = page.get_text()
print(text)

# Render and save the page as an image
pix = page.get_pixmap() 
pix.save(f"page-{page.number}.png")

# get all links on a page
links = page.get_links()
print(links)

# Render and save all the pages as images
for i in range(doc.page_count):
  page = doc.load_page(i)
  pix = page.get_pixmap()
  pix.save("page-%i.png" % page.number)

# get the links on all pages
for i in range(doc.page_count):
  page = doc.load_page(i)
  link = page.get_links()
  print(link)