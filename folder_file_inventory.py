# Scan a folder and create a text file that lists
# information about every file found.

import os

# Asks the user for the folder to scan.
folder = input("Enter the folder path: ")

# Open the report file.
reportFile = open("FileInventoryReport.txt", "w")

reportFile.write("File Inventory Report\n")
reportFile.write("=" * 30 + "\n\n")

# Walk through all folders.
for folderName, subfolders, filenames in os.walk(folder):

    # Loop through every file.
    for filename in filenames:

        # Get the extension.
        name, extension = os.path.splitext(filename)

        if extension == "":
            extension = "No Extension"
        
        # Full path to the file.
        filePath = os.path.join(folderName, filename)

        # Get file size.
        fileSize = os.path.getsize(filePath)


        # Write information to the report.
        reportFile.write("Name: " + filename + "\n")
        reportFile.write("Extension: " + extension + "\n")
        reportFile.write("Location: " + folderName + "\n")
        reportFile.write("Size: " + str(fileSize) + " bytes\n")
        reportFile.write("-" * 30 + "\n")


# Close the file.
reportFile.close()

print("Inventory report created successfully.")