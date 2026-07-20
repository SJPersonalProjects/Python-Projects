# Bactch File Renamer.

import os
import logging

# Configure logging
logging.basicConfig(
    filename="RenameLog.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder = input("Enter folder path: ")
folder = os.path.abspath(folder)

prefix = input("Enter prefix (leave blank for none): ")
suffix = input("Enter suffix (leave blank for none): ")

numbering = input("Add numbering? (yes/no): ").lower()

counter = 1

print("\nPreview")
print("-" * 40)

renameList = []

for filename in os.listdir(folder):

    filePath = os.path.join(folder, filename)

    # Skip folders.
    if not os.path.isfile(filePath):
        continue

    name, extension = os.path.splitext(filename)

    # Validate filename
    if name == "":
        print("Skipping invalid filename: ", filename)
        continue

    newName = prefix + name + suffix

    if numbering == "yes":
        newName += "_" + str(counter)

    newName += extension

    renameList.append((filename, newName))

    print(filename, "--->", newName)

    counter += 1

choice = input("\nRename these files? (yes/no): ").lower()

if choice == 'yes':

    for oldName, newName in renameList:

        oldPath = os.path.join(folder, oldName)
        newPath = os.path.join(folder, newName)

        os.rename(oldPath, newPath)

        logging.info(f"Renamed: {oldName} --> {newName}")


    print("\nAll files renamed successfully!")
    print("Log saved to RenameLog.log")

else:
    print("\nOperation cancelled.")