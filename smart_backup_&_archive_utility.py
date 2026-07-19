# Smart Backup & Archive Utility.

import os
import zipfile
import datetime

# Ask the user for the fodler to back up.
folder = input("Enter the folder path: ")
folder = os.path.abspath(folder)

# Ask which files extension to skip.
skipExtensions = input(
    "Enter extensions to skip (comma separated, e.g. .tmp, .log, .mp4): ")

skipExtensions = skipExtensions.lower().split(",")

# Ask which folders to skip.
skipFolders = input(
    "Enter folder names to skip (comma separated, e.g. Cache, Temp): "
)

skipFolders = skipFolders.split(",")

# Find the next backup number.
number = 1

while True:
    zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"

    if not os.path.exists(zipFilename):
        break

    number += 1

print("Creating", zipFilename)

backupZip = zipfile.ZipFile(zipFilename, "w")

# Backup log.
logFile = open("BackupLog.txt", "a")

currentTime = datetime.datetime.now()

logFile.write("Backup File: " + zipFilename + "\n")
logFile.write("Folder: " + folder + "\n")
logFile.write("Date & Time: " + str(currentTime) + "\n")
logFile.write("\nIncluded Files\n")
logFile.write("-" + 40 + "\n")

# Walk through every folder.
for folderName, subfolders, filenames in os.walk(folder):

    # Skip selected folders.
    subfolders[:] = [sub for sub in subfolders if sub not in skipFolders]

    backupZip.write(folderName)

    for filename in filenames:

        # Skip previous backup ZIP files.
        if filename.startswith(os.path.basename(folder) + "_") and filename.endswith(".zip"):
            continue

        name, extension = os.path.splitext(filename)

        # Skip unwanted extensions.
        if extension.lower() in skipExtensions:
            continue

        filePath = os.path.join(folderName, filename)

        backupZip.write(filePath)

        logFile.write(filePath + "\n")

backupZip.close()

logFile.write("\nVerification\n")
logFile.write("-" * 40 + "\n")

# Verify ZIP contents.
verifyZip = zipfile.ZipFile(zipFilename)

for file in verifyZip.namelist():
    logFile.write(file + "\n")

verifyZip.close()

logFile.write("-" * 40 + "\n\n")
logFile.close()

print("Backup completed successfully.")
print("Archive verified")
print("Backup log created.")


