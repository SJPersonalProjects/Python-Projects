# PDF Merger Tool.

import PyPDF2

# Create a PDF writer.
writer = PyPDF2.PdfWriter()

# Ask the user how many pdfs to merge.
count = int(input("How many PDF files do you want to merge? "))

# Read each PDF
for i in range(count):
    filename = input(f"Enter PDF file {i + 1}: ")

    with open(filename, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        # Add every page to the writer.
        for page in reader.pages:
            writer.add_page(page)

# Save the merged PDF
output_name = input("Enter the output PDF filename: ")

with open(output_name, "wb") as output_file:
    writer.write(output_file)

print("PDFs merged successfully!")
print(f"Saved as '{output_name}'")