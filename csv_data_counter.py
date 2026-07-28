# CSV Data Counter.

import csv

# Ask the user for the CSV filename.
filename = input("Enter the CSV filename: ")

# Dictionary to store counts.
fruits_count = {}

# Open the CSV file.
with open(filename, "r", newline="") as csv_file:
    reader = csv.reader(csv_file)

    # Skip the header.
    next(reader)

    # Count each fruit.
    for row in reader:
        fruit = row[0]

        if fruit in fruits_count:
            fruits_count[fruit] += 1
        else:
            fruits_count[fruit] = 1

# Display the results.
print("\nFruit Counts")
print("-" * 20)

for fruit, count in fruits_count.items():
    print(f"{fruit}: {count}")