# Folder Inventory Report
# List all files in a folder along with their sizes and
# calculate the total folder size.

import os

# Ask the user for the folder path
folder_path = input("Enter the folder path: ")

# Check if the folder exists.
if os.path.isdir(folder_path):

    total_size = 0

    print("\nFolder Inventory Report")
    print("-" * 40)

    # Loop through every item in the folder.
    for item in os.listdir(folder_path):

        # Create the complete path.
        item_path = os.path.join(folder_path, item)

        # Process only files.
        if os.path.isfile(item_path):

            # Get the file size.
            file_size = os.path.getsize(item_path)

            # Add the file size to the total.
            total_size += file_size

            # Display the file name and its size.
            print(f"{item} ---> {file_size} bytes")

    print("-" * 40)
    print("Total Folder Size: ", total_size, "bytes")

else:
    print("The folder does not exist.")