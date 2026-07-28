# Word Text Reader.
import docx

# Ask the user for the word document.
filename = input("Enter the Word document filename: ")

# Open the document.
document = docx.Document(filename)

# Display all paragraphs.
print("\nDocument Contents:\n")

for paragraph in document.paragraphs:
    print(paragraph.text)