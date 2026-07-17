# File extension counter.

import os

# Folder to scan.
folder = input("Enter the folder path: ")

# Dictionary to store extension counts.
extensionCount = {}

# Walk through the folder and its subfolders.
for folderName, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        # Get the file extension.
        name, extension = os.path.splitext(filename)

        # Handle files with no extensions.
        if extension == "":
            extension = "No Extension"

        # Count the extensions.
        if extension in extensionCount:
            extensionCount[extension] += 1
        else:
            extensionCount[extension] = 1

# Display the results.
print("\nFile Extension Counts")
print("-" * 25)

for extension in extensionCount:
    print(extension + " :", extensionCount[extension])
