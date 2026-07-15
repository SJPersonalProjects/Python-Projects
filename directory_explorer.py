# Directory Explorer.
# Display the current working directory and list all the files and folders.

import os

# Get the current working directory.
current_directory = os.getcwd()

print("Current Working Directory:")
print(current_directory)

# Get all the items in the current directory.
items = os.listdir(current_directory)

print("\nContents:")
print("-" * 30)

# Checks whether each item is a file or folder.
for item in items:

    # Create the complete path to the item.
    item_path = os.path.join(current_directory, item)

    if os.path.isfile(item_path):
        print(f"{item} ---> File")
    
    elif os.path.isdir(item_path):
        print(f"{item} ---> Folder")