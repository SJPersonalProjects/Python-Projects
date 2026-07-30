# File Auto Opener.

import os
import subprocess

# Ask the user for the filename.
filename = input("Enter the filename: ")

# Check if the file exists.
if os.path.exists(filename):
    print("Opening file...")

    # Open teh file with the default application (linux)
    subprocess.Popen(["xdg-open", filename])
else:
    print("Error: File not found.")