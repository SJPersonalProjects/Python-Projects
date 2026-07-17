# Duplicate filenames detector.

import os

# Ask the user for the folder to scan.
folder = input("Enter the folder path: ")

# Dictionary to store filenames and their locations.
fileNames = {}

# Open the report file.
reportFile = open("DuplicateFileNamesReport.txt", "w")

reportFile.write("Duplicate Filenames Report\n")
reportFile.write("=" * 30 + "\n\n")

# Walk through all folders.
for folderName, subfolders, filenames in os.walk(folder):

    # Check every file.
    for filename in filenames:

        # Full path of the file.
        filePath = os.path.join(folderName, filename)

        # Store the file path in the dictionary.
        if filename in fileNames:
            fileNames[filename].append(filePath)
        else:
            fileNames[filename] = [filePath]


# Write duplicate filenames to the report.
for filename in fileNames:

    if len(fileNames[filename]) > 1:

        reportFile.write("Filename: " + filename + "\n")

        for location in fileNames[filename]:
            reportFile.write(" " + location + "\n")

        reportFile.write("-" * 30 + "\n")

reportFile.close()

print("Duplicate filename report created successfully.")

