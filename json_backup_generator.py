# JSON Backup Generator.

import json

# Sample program data.
program_data = {
    "project": "Student Management Ssytem",
    "version": "1.0",
    "students": [
        {
            "name": "Ali",
            "marks": 88
        },
        {
            "name": "Sara",
            "marks": 95
        },
        {
            "name": "Ahmed",
            "marks": 81
        }
    ]
}

# Convert Python object to JSON string.
json_data = json.dumps(program_data, indent=4)

# Save JSON string to a backup file.
with open("backup.json", "w") as file:
    file.write(json_data)

print("Backup created successfully!")

# Read the backup file.
with open("backup.json", "r") as file:
    backup_data = file.read()

# Restore the data.
restored_data = json.loads(backup_data)

print("\nRestored Data")
print("-" * 30)
print(restored_data)