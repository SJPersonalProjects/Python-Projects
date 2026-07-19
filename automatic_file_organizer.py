# Automatic Files Organizer.

import os
import shutil

# Ask the user for the folder to organize.
folder = input("Enter the folder path: ")

# Walk through the folder.
for folderName, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        # Get the file extension.
        name, extension = os.path.splitext(filename)
        extension.lower()

        # Decide the destination folders.
        if extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            destinationFolder = "Images"

        elif extension in [".pdf", ".avi", ".mkv"]:
            destinationFolder = "Videos"

        elif extension in [".zip", ".avi", ".7z"]:
            destinationFolder = "Archives"

        elif extension == ".py":
            destinationFolder = "Python Files"

        else:
            destinationFolder = "Others"
        
        # Create the destination folder if it doesn't exist.
        destinationPath = os.path.join(folder, destinationFolder)

        if not os.path.exists(destinationPath):
            os.mkdir(destinationPath)
        
        # Full Paths.
        sourceFile = os.path.join(folderName, filename)
        destinationFile = os.path.join(destinationPath, filename)

        # Don't move files that are already in the correct folders.
        if sourceFile != destinationFile:
            shutil.move(sourceFile, destinationFile)
            
            print(filename + " moved to " + destinationFolder)

print("Files organized successfully.")