# Project backup manager.

import os
import zipfile
import datetime

# Ask the user for the folder to back up.
folder = input("Enter the fodler path: ")

# Remove any trailing slash.
folder = os.path.abspath(folder)

# Determine the backup.
number = 1

while True:
    zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"

    if not os.path.exists(zipFilename):
        break

    number += 1

print("Creating", zipFilename + "...")

# Create the ZIP file.
backupZip = zipfile.ZipFile(zipFilename, "w")

# Walk through the folder.
for folderName, subfolders, filenames in os.walk(folder):

    # Add the current folder.
    backupZip.write(folderName)

    # Add each file.
    for filename in filenames:

        # Skip previous backup ZIP files.
        if filename.startswith(os.path.basename(folder) + "_") and filename.endswith(".zip"):
            continue

        filePath = os.path.join(folderName, filename)
        backupZip.write(filePath)


backupZip.close()

# Write the backup logs.
logFile = open("BackupLog.txt", 'a')

currentTime = datetime.datetime.now()

logFile.write("Backup File: " + zipFilename + "\n")
logFile.write("Folder: " + folder + "\n")
logFile.write("Date & Time: " + str(currentTime) + "\n")
logFile.write("-" + 40 + "\n")

logFile.close()

print("Backup completed successfully.")