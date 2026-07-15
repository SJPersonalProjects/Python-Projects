# File Information Viewer.
# Display information about a file.

import os

# As the user for a file path.
file_path = input("Enter the file path: ")

# Check if the file exists.
if os.path.exists(file_path):

    # Display file information.
    print("\nFile Information")
    print("-" * 30)
    print("Absolute Path: ", os.path.abspath(file_path))
    print("File Name: ", os.path.basename(file_path))
    print("Directory: ", os.path.dirname(file_path))
    print("Size: ", os.path.getsize(file_path), "bytes")

else:
    print("The file doesn't exist.")