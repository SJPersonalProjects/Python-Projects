# Date Filename Renamer.

import os
import re

# Regular expression for MM-DD-YYYY
datePattern = re.compile(r'''
^(.*?)
((0|1)?\d)
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*)$
''', re.VERBOSE)

# Ask the user for the folder name.
folder = input("Enter the folder path: ")

preview = []

# Search for matching filenames.
for folderName, subfolders, filenames in os.walk(folder):

    for filename in filenames:

        match = datePattern.search(filename)

        if match is None:
            continue

        beforePart = match.group(1)
        monthPart = match.group(2)
        dayPart = match.group(4)
        yearPart = match.group(6)
        afterPart = match.group(8)

        newFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart

        oldPath = os.path.join(folderName, filename)
        newPath = os.path.join(folderName, newFilename)

        preview.append((oldPath, newPath))


# Preview
print("\nPreview")
print("-" * 40)

for oldName, newName in preview:
    print(os.path.basename(oldName), "->", os.path.basename(newName))

# Ask for confirmation.
choice = input("\nRename these files? (y/n)")

if choice.lower() == "y":

    for oldName, newName in preview:
        os.rename(oldName, newName)

    print("Files renamed successfully.")

else:
    print("No files were renamed.")