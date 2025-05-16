from pypdf import PdfReader, PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

# Optional: sort files alphabetically
files.sort()

# Read each PDF and add its pages
for file in files:
    reader = PdfReader(file)
    for page in reader.pages:
        merger.add_page(page)

# Write the merged output
with open("merged-pdf.pdf", "wb") as f:
    merger.write(f)
