# CSV File Reader.

import csv

# Ask the user for the CSV filename.
filename = input("Enter the CSV filename: ")

# Open the CSV file.
with open(filename, "r", newline="") as csv_file:
    reader = csv.reader(csv_file)

    # Read and display each row.
    for row in reader:
        print(row)