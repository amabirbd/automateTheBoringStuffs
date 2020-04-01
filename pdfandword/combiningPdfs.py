import PyPDF2, os

pdfFiles =[]

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
    
pdfFiles.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# loop through all the pdf
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# loop through all pages except the first and add
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# save the resulting pdf to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()