# PDF Page Counter.
import PyPDF2

# Ask the user for the PDF file.
filename = input("Enter the PDF filename: ")

# Open the PDF file.
with open(filename, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    # Display the total number of pages.
    print(f"\nTotal pages: {len(reader.pages)}")