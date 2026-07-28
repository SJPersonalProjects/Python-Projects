# Document Converter Organizer.

import os
import shutil

# Ask the user for the folder to organize.
folder = input("Enter the folder path: ")

# Create destination folders.
pdf_folder = os.path.join(folder, "PDF Files")
word_folder = os.path.join(folder, "Word Files")

os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(word_folder, exist_ok=True)

# scan the folder.
for filename in os.listdir(folder):

    file_path = os.path.join(folder, filename)

    # Skip folders.
    if os.path.isdir(file_path):
        continue

    # Move PDf files.
    if filename.lower().endswith(".pdf"):
        shutil.move(file_path, os.path.join(pdf_folder, filename))
        print(f"Moved: {filename}")

    # Move Word Files.
    elif filename.lower().endswith(".docx"):
        shutil.move(file_path, os.path.join(word_folder, filename))
        print(f"Moved: {filename}")

print("\nOrganization complete!")