# Python Data Backup Generator
# Save a dictionary to a .py file using pprint.pformat()
# and then import it to verify the backup.

import pprint
import importlib

# Data to back up.
student = {
    "name": "Alex",
    "age": 21,
    "skills": ["Python", "Git", "Linux"],
    "marks": {
        "Python": 95,
        "Git": 90,
        "Linux": 88
    }
}

# Create the backup file.
backup_file = open("backup_data.py", "w")

# Write the dictionary as python code.
backup_file.write("data = ")
backup_file.write(pprint.pformat(student))

# Close the file.
backup_file.close()

print("Backup created successfully!")

# Import the backup file.
backup_data = importlib.import_module("backup_data")

# Display the backed up data.
print("\nRecovered Data:")
print(backup_data.data)