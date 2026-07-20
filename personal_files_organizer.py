# Personal Files Organizer.

import os
import shutil
import zipfile
import logging

# Configure logging
logging.basicConfig(
    filename="OrganizerLog.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# File categories.
categories = {
    "Images": [".jpg", ".jjeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python Files": [".py"],
    "Others": []
}

folder = input("Enter folder path: ")
folder = os.path.abspath(folder)

try:
    if not os.path.exists(folder):
        raise FileNotFoundError("Folder doesn't exist.")

    print("\nOrganizing files...\n")

    # Organize files
    for filename in os.listdir(folder):

        filePath = os.path.join(folder, filename)

        # Skip folders.
        if not os.path.isfile(filePath):
            continue

        name, extension = os.path.splitext(filename)
        extension = extension.lower()

        destinationFolder = "Others"

        # Find matching category.
        for category, extensions in categories.items():
            if extension in extensions:
                destinationFolder = category
                break

        destinationPath = os.path.join(folder, destinationFolder)

        # Create fodler if missing.
        if not os.path.exists(destinationPath):
            os.makedirs(destinationPath)
            logging.info(f"Created folders: {destinationFolder}")

        newPath = os.path.join(destinationPath, filename)

        shutil.move(filePath, newPath)

        print(f"Moved: {filename} --> {destinationFolder}")

        logging.info(f"Moved {filename} to {destinationFolder}")

    # Create backup ZIP.
    backupNumber = 1

    while True:
        zipFilename = f"OrganizedBackup.{backupNumber}.zip"
        if not os.path.exists(zipFilename):
            break

        backupNumber += 1

    backupZip = zipfile.ZipFile(zipFilename, "w", zipfile.ZIP_DEFLATED)

    for folderName, subfolders, filenames in os.walk(folder):

        for filename in filenames:

            filePath = os.path.join(folderName, filename)

            # Don't include previous backups.
            if filename.startswith("OrganizedBackup_") and filename.endswith(".zip"):
                continue

            backupZip.write(filePath)

            logging.info(f"Added to ZIP: {filePath}")

    backupZip.close()

    print("\nBackup created: ", zipFilename)
    logging.info(f"Backup created: {zipFilename}")

except FileNotFoundError as error:
    print(error)

    logging.error(error)

except Exception as error:

    print("Unexpected error: ", error)

    logging.error(error)


print("\nFinished.")
print("Log saved to OrganizerLog.log")