# CSV Header Remover.

import os
import csv

# Ask the user for the folder.
source_folder = input("Enter the folder path: ")

# Create output folder.
output_folder = os.path.join(source_folder, "Cleaned CSV Files")
os.makedirs(output_folder, exist_ok=True)

# Process every CSV file.
for filename in os.listdir(source_folder):

    if filename.lower().endswith(".csv"):

        input_file = os.path.join(source_folder, filename)
        output_file = os.path.join(output_folder, filename)

        with open(input_file, "r", newline="") as csv_input:
            reader = csv.reader(csv_input)

            with open(output_file, "w", newline="") as csv_output:
                writer = csv.writer(csv_output)

                # Skip the header.
                next(reader)

                # Write remaining rows.
                for row in reader:
                    writer.writerow(row)

                
        print(f"Processed: {filename}")

print("\nAll CSV files have been cleaned.")

