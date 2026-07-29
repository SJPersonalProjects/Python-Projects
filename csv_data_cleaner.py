# CSV Data Cleaner.

import csv

# Ask the user for the csv filename.
filename = input("Enter the CSV filename: ")

cleaned_rows = []

# Open the CSV file.
with open(filename, "r", newline="") as csv_file:
    reader = csv.reader(csv_file)

    # Save the header.
    header = next(reader)
    cleaned_rows.append(header)

    # Process each row.
    for row in reader:
        # Replace empty author.
        if row[2] == "":
            row[2] = "Unknown Author"
        
        # Validate year.
        try:
            int(row[3])
        except ValueError:
            row[3] = "Unknown"

        # Validate copies.
        try:
            int(row[4])
        except ValueError:
            row[4] = "0"

        cleaned_rows.append(row)

# Save cleaned data.
output_file = "cleaned_" + filename

with open(output_file, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    for row in cleaned_rows:
        writer.writerow(row)

print("CSV cleaned successfully!")
print(f"Saved as '{output_file}'")