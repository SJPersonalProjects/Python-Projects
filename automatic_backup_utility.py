# Automatic Backup Utility.

import os
import zipfile
import logging

# Configure logging.
logging.basicConfig(
    filename="BackupLog.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ask the user for the folder.
folder = input("Enter the folder path: ")
folder = os.path.abspath(folder)

# Create a versioned backup name.
backupNumber = 1

while True:

    zipFilename = f"backup_{backupNumber}.zip"

    if not os.path.exists(zipFilename):
        break

    backupNumber += 1

# Create the ZIP file.
backupZip = zipfile.ZipFile(zipFilename, "w", zipfile.ZIP_DEFLATED)

print("\nCreating backup...\n")

# Walk through the folder.
for folderName, subfolders, filenames, in os.walk(folder):

    for filename in filenames:

        filePath = os.path.join(folderName, filename)

        backupZip.write(filePath)

        logging.info(f"Added: {filePath}")

        print("Added: ", filePath)

backupZip.close()

logging.info(f"Backup created: {zipFilename}")

print("\nBackup completed!")
print("ZIP File: ", zipFilename)
print("Log File: BackupLog.log")