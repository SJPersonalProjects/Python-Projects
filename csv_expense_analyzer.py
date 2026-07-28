# CSV Expense Analyzer.

import csv

# Ask teh user for the CSV filename.
filename = input("Enter the CSV filename: ")

# Variables for statistics.
total = 0
highest = 0
lowest = None
category_totals = {}

# Open the CSV file.
with open(filename, "r", newline="") as csv_file:
    reader = csv.reader(csv_file)

    # Skip the header.
    next(reader)

    # Read each expense.
    for row in reader:
        category = row[0]
        amount = float(row[1])

        # Total expenses.
        total += amount

        # Highest expense.
        if amount > highest:
            highest = amount

        # Lowest expense.
        if lowest is None or amount < lowest:
            lowest = amount

        # Category-wise spending.
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
        
# Display results.
print("\nExpense Report")
print("-" * 25)
print(f"Total Expenses : ${total}")
print(f"Highest Expense : ${highest}")
print(f"Lowest Expense : ${lowest}")

print("\nCategory-wise Spending:")
for category, amount in category_totals.items():
    print(f"{category}: ${amount}")