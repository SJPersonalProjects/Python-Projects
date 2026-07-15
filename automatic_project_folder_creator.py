# Automatic Project Folder Creator.
# Create a complete project folder structure.

import os

# Ask the user for the project name.
project_name = input("Enter the project name: ")

# list of folders to create.
folders = [
    'src',
    'docs',
    'assets',
    'tests',
    'data'
]

# Create the main project folder.
os.makedirs(project_name, exist_ok=True)

# Create each subfolder.
for folder in folders:

    # Create the complete folder path
    folder_path = os.path.join(project_name, folder)

    # Create the folder.
    os.makedirs(folder_path, exist_ok=True)


print("\nProject folder structure created successfully!")