# PDF Watermark Generator.

import PyPDF2
import os

# Ask for the watermark file.
watermark_file = input("Enter the watermark PDF filename: ")

# Load the watermark page.
with open(watermark_file, "rb") as watermark_pdf:
    watermark_reader = PyPDF2.PdfReader(watermark_pdf)
    watermark_page = watermark_reader.pages[0]

    # Ask how many PDFs to watermark.
    count = int(input("How many PDF files do you want to watermark? "))

    for i in range(count):

        pdf_name = input(f"\nEnter PDF file {i + 1}: ")
        
        with open(pdf_name, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()


            # Watermark every page.
            for page in reader.pages:
                page.merge_page(watermark_page)
                writer.add_page

            # Save the new PDF
            folder = os.path.dirname(pdf_name)
            filename = os.path.basename(pdf_name)

            output_name = os.path.join(folder, "Watermarked_" + filename)

            with open(output_name, "wb") as output_file:
                writer.write(output_file)

            print(f"Created: {output_name}")

print("\nAll PDFs have been watermarked successfully!")

