# Working with PDF Documents

## PDF Overview
- PDF stands for Portable Document Format, using the `.pdf` extension.
- Focus on reading text and creating new PDFs from existing ones.
- Use **PyPDF2 version 1.26.0** for PDF manipulation.

---

## Extracting Text from PDFs
- PyPDF2 can extract text but not images or charts.
- Use `PdfFileReader` to read PDF files and `extractText()` to get text content.
- Text extraction may not be perfect due to PDF formatting.

---

## Decrypting PDFs
- Encrypted PDFs require a password to access.
- Use the `decrypt()` method with the correct password to read encrypted PDFs.
- A new `PdfFileReader` object must be created after decryption.

---

## Creating and Modifying PDFs
- Use `PdfFileWriter` to create new PDFs by copying pages from existing ones.
- Capabilities include:
  - Rotating pages
  - Overlaying content
  - Encrypting PDFs
- Limitations:
  - Cannot edit existing PDFs directly.

---

# Working with Word Documents

## Word Document Overview
- Word documents use the `.docx` extension and have a structured format.
- Use the **python-docx** module to create and modify Word documents.

---

## Reading Word Documents
- Use `docx.Document()` to open and read `.docx` files.
- Access **paragraphs** and **runs** to manipulate text and styles.

---

## Creating Word Documents
- Create new documents with `docx.Document()` and add paragraphs or headings.
- Methods for content addition:
  - `add_paragraph()`
  - `add_heading()`
- Additional features:
  - Adding line breaks
  - Inserting pictures

---

## Styling in Word Documents
- Styles can be applied to paragraphs and runs.
- Default styles are available, and custom styles can be created in Word.

---

# Combining PDFs and Word Documents

## Project: Combining PDFs
- Write a Python program to merge multiple PDFs while excluding specific pages.
- Use `os.listdir()` to find PDF files and `PdfFileWriter` to create the output.

---

## Creating PDFs from Word Documents
- Use **pywin32** to convert Word documents to PDFs on Windows.
- Create a Word document with **python-docx** and save it as a PDF using Word's COM interface.

---

# Summary of Key Points
- PDFs and Word documents are complex formats requiring specific libraries for manipulation.
- **PyPDF2** is used for PDFs, while **python-docx** is used for Word documents.
- Both formats have limitations in editing and require careful handling of text extraction and processing.

## Working with PDFs

### Extracting Text from PDFs
```python
import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()
pdfFileObj.close()
```
---

## Working with PDFs

### Extracting Text from PDFs

```python
import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()
pdfFileObj.close()
```

### Decrypting Encrypted PDFs

```python
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
```
### Combining Multiple PDFs
```python
import PyPDF2
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
```
### Rotating Pages in a PDF

```python
import PyPDF2
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
```
### Adding a Watermark to a PDF

```python
import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
```

### Encrypting a PDF
```python

import PyPDF2
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
```

### Merging Multiple PDFs in a Directory
```python
import PyPDF2, os
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
```
## Working with Word Documents
### Reading Word Documents
```python
import docx
doc = docx.Document('demo.docx')
len(doc.paragraphs)
doc.paragraphs[0].text
doc.paragraphs[1].text
len(doc.paragraphs[1].runs)
doc.paragraphs[1].runs[0].text
doc.paragraphs[1].runs[1].text
doc.paragraphs[1].runs[2].text
doc.paragraphs[1].runs[3].text
```
### Extracting All Text from a Word Document
```python
import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
```
### Modifying Styles in Word Documents
```python
import docx
doc = docx.Document('demo.docx')
doc.paragraphs[0].style = 'Normal'
doc.paragraphs[1].runs[0].style = 'QuoteChar'
doc.paragraphs[1].runs[1].underline = True
doc.paragraphs[1].runs[3].underline = True
doc.save('restyled.docx')
```
### Creating Word Documents
```python
import docx
doc = docx.Document()
doc.add_paragraph('Hello, world!')
doc.save('helloworld.docx')
```

### Adding Paragraphs and Runs
```python
import docx
doc = docx.Document()
paraObj1 = doc.add_paragraph('This is a second paragraph.')
paraObj1.add_run(' This is added to the second paragraph.')
doc.save('multipleParagraphs.docx')
```

### Adding Headings
```python
doc.add_heading('Header 0', 0)
doc.add_heading('Header 1', 1)
doc.save('headings.docx')
```

### Adding Pictures to a Word Document
```python
doc.add_picture('zophie.png', width=docx.shared.Inches(1), height=docx.shared.Cm(4))
```
### Converting Word Documents to PDF
```python
import win32com.client
import docx
wordFilename = 'your_word_document.docx'
pdfFilename = 'your_pdf_filename.pdf'
doc = docx.Document()
doc.save(wordFilename)
wdFormatPDF = 17
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
```