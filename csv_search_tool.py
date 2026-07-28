# CSV Search Tool.

import csv

# Ask the user for the CSV filename.
filename = input("Enter the CSV filename: ")

# Ask for the CSV file.
search_value = input("Enter the value to search for: ").lower()

# Open the CSV file.
with open(filename, "r", newline="") as csv_file:
    reader = csv.reader(csv_file)

    # Read the header.
    header = next(reader)

    found = False

    # Search each row.
    for row in reader:

        # Check every column in the row.
        for value in row:
            if search_value == value.lower():
                print(row)
                found = True
                break

# Display message if nothing was found.
if not found:
    print("No matching records found.")