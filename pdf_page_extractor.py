# PDF Page Extractor.

import PyPDF2

# Ask the user for the PDF file.
input_file = input("Enter the PDF filename: ")

# Open the PDF.
with open(input_file, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()

    # Ask for page numbers.
    pages = input("Enter page numbers to extract (comma-separated): ")

    # Convert the input into a list of integers.
    page_numbers = pages.split(",")

    # Extract each page.
    for page in page_numbers:
        page_index = int(page.strip()) - 1

        if 0 <= page_index < len(reader.pages):
            writer.add_page(reader.pages[page_index])
        else:
            print(f"Page {page.strip()} does not exist.")
        
    # Save the extracted pages.
    output_file = input("Enter the output PDF filename: ")

    with open(output_file, "wb") as output_pdf:
        writer.write(output_pdf)

print("Selected pages extracted successfully!")
print(f"Saved as '{output_file}'")