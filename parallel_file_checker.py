# Parallel File Checker.

import os
import threading
from datetime import datetime

# Ask the user for the folder.
folder = input("Enter the folder path: ")

# Store results from all threads.
results = []

# Function that checks one file.
def check_file(filepath):
    file_info = {
        "Name": os.path.basename(filepath),
        "Extension": os.path.splitext(filepath)[1],
        "Size (bytes)": os.path.getsize(filepath),
        "Last Modifier": datetime.fromtimestamp(
            os.path.getmtime(filepath)
        ).strftime("%Y-%m-%d %H:%M:%S")
    }

    results.append(filepath)

threads = []

# Create one thread for each file.
for filename in os.listdir(folder):

    filepath = os.path.join(folder, filename)

    if os.path.isfile(filepath):

        thread = threading.Thread(target=check_file, args=(filepath,))

        threads.append(thread)
        thread.start()


# Wait for every thread to finish
for thread in threads:
    thread.join()

# Display report.
print("\nFile Report")
print("-" * 60)

for file in results:
    print(f"Name            :       {file['Name']}")
    print(f"Extension       :       {file['Extension']}")
    print(f"Size            :       {file['Size (bytes)']} bytes")
    print(f"Last Modified   :       {file['Last Modified']}")
    print("-" * 60)

