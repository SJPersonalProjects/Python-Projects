# Bulk file rename.

import os

# Ask the user for the folder and prefix.
folder = input("Enter the folder path: ")
prefix = input("Enter the prefix to add: ")

# Walk through all folders.
for folderName, subfolders, filenames in os.walk(folder):

    # Rename each file.
    for filename in filenames:

        # Separate filename and extension.
        name, extension = os.path.splitext(filename)

        # Create the new filename.
        newFilename = prefix + name + extension

        # Create full paths
        oldFilePath = os.path.join(folderName, filename)
        newFilePath = os.path.join(folderName, newFilename)

        # Rename the file.
        os.rename(oldFilePath, newFilePath)

        print(filename + " --> " + newFilename)

print("All the files have been renamed successfully.")