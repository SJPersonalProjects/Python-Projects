# Empty Folder Finder.

import os

# Asks the user for the folder to scan.

folder = input("Enter the folder path: ")

# Open the report file.
reportFile = open("EmptyFoldersReport.txt", "w")

reportFile.write("Empty Folders Report\n")
reportFile.write("=" * 30 + "\n\n")

# Walk through every folder.
for folderName, subfolders, filenames in os.walk(folder):
    # Checks if the folder is empty.
    if len(subfolders) == 0 and len(filenames) == 0:

        reportFile.write(folderName + "\n")

reportFile.close()

print("Empty folder report created successfully.")