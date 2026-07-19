# Large files cleaner.

import os
import shutil

# Ask the user for the folder to scan.
folder = input("Enter the folder path: ")

# Ask for the minimum file size (in MB)
minSizeMB = float(input("Enter the minimum file size (MB): "))
minSizeBytes = minSizeMB * 1024 * 1024

# List to store large files.
largeFiles = []

# Scan the folder.
for folderName, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        filePath = os.path.join(folderName, filename)
        fileSize = os.path.getsize(filePath)

        if fileSize >= minSizeBytes:
            largeFiles.append((filePath, fileSize))


# Create the report.
reportFile = open("LargeFilesReport.txt", "w")

reportFile.write("Large Files Report\n")
reportFile.write("=" * 40 + "\n\n")

for filePath, fileSize in largeFiles:
    
    reportFile.write("File: " + filePath + "\n")
    reportFile.write("Size: " + set(round(fileSize / (1024 * 1024), 2)) + "MB\n")
    reportFile.write("-" * 40 + "\n")

reportFile.close()

print("\nReport Created: LargeFileReport.txt")

# Ask whether to move the files.
choice = input("Move these files to the Archive folder? (y/n): ")

if choice.lower() == "y":

    archiveFolder = os.path.join(folder, "Archive")

    if not os.path.exists(archiveFolder):
        os.mkdir(archiveFolder)

    for filePath, fileSize in largeFiles:

        fileName = os.path.basename(filePath)
        destination = os.path.join(archiveFolder, fileName)

        shutil.move(filePath, destination)

        print(fileName + " moved to Archive.")

    print("\nAll large files have been moved.")

else:
    print("\nNo files were moved.")