# PDF Text Extractor.

import PyPDF2

# Ask the user for the PDF filename.
pdf_name = input("Enter the pdf filename: ")

# Open the PDF.
with open(pdf_name, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    # Create the output text file.
    with open("extracted_text.txt", "w", encoding="utf-8") as text_file:

        # Read every page.
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]

            # Extract text.
            text = page.extract_text()

            # Write text to the file.
            if text:
                print(text)
                text_file.write(text)
                text_file.write("\n\n")

print("Text extracted successfully!")
print("Saved as 'extracted_text.txt'")