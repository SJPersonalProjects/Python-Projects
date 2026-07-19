# Folder Scanner Logger.

import os
import logging

# Configure logging.
logging.basicConfig(

    filename="FolderScanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder = input("Enter the folder path: ")
folder = os.path.abspath(folder)

totalFolders = 0
totalFiles = 0

logging.info("Folder scan started.")
logging.info(f"Scanning: {folder}")

for folderName, subfolders, filenames in os.walk(folder):
    totalFolders += 1
    logging.info(f"Visited Folders: {folderName}")

    totalFiles += len(filenames)

logging.info("Folder scan completed.")
logging.info(f"Total Folders: {totalFolders}")
logging.info(f"Total Files: {totalFiles}")

print("\nScan Completed")
print("-" * 30)
print("Folders: ", totalFolders)
print("Files: ", totalFiles)

reportFile = open("ScanReport.txt", "w")

reportFile.write("Folder Scan Report\n")
reportFile.write("-" * 30 + "\n")
reportFile.write("Scanned Folder: " + folder + "\n")
reportFile.write("Total Folders: " + str(totalFolders) + "\n")
reportFile.write("Total Files: " + str(totalFiles) + "\n")

reportFile.close()

print("Report saved to ScanReport.txt")
print("Log saved to FolderScanner.log")