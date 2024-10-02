import PyPDF2 as p
import re



pdf = p.PdfReader(open(r"D:\OfficeDocumentsOfShadAhmed\MyProfessionalRepository\Professional\InvoiceReaderSoftware\abc2.pdf", "rb"))
pdf=pdf.pages[:]
for i in pdf:
    print(i.extract_text())
    print("")