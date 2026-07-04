# Bill Splitter: Splits the bill share between diners.

total_bill = float(input("Enter the total bill amount: "))
number_of_diners = float(input("Enter the number of diners: "))

share_per_person = total_bill / number_of_diners

print(f"Each person should pay: {share_per_person}")