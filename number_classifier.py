# Classifies a number into positive or negative or zero.

number = int(input("Enter any integer: "))

if number < 0:
    print(f"{number} is a negative integer")
elif number > 0:
    print(f"{number} is a positive integer")
else:
    print(f"{number} is zero")