import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)


pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

# for encrypted pdfs
print(pdfReader.isEncrypted)
# pdfReader.decrypt('password')

# copying from one pdf to another
pdfFile1 = open('meetingminutes.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdfFile1)
pdf2Reader = PyPDF2.PdfFileReader(pdfFile2)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFile1.close()
pdfFile2.close()

# Rotating Pages
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

# overlaying pages
minutesFirstPage = pdfReader.getPage(0)
pdfWaterMarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWaterMarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pagenum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pagenum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkdCover', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()

# encrypting pdf
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pagnum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')
resultPdf = open('ecryptedminutes.pdf', 'wb')
resultPdf.close()