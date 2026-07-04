# Calculator with functions.

def addition(value_one, value_two):
    return value_one + value_two

def subtraction(value_one, value_two):
    return value_one - value_two

def division(value_one, value_two):
    return value_one / value_two

def multiplication(value_one, value_two):
    return value_one * value_two

def remainder(value_one, value_two):
    return value_one % value_two

operation = input("\nWhat operation would you wanna do:_\nAddition\nSubtraction\nDivision\nMultiplication\nRemainder\n\nI choose: ")

value_one = float(input("Enter value 1: "))
value_two = float(input("Enter value 2: "))

if operation.lower() == "addition":
    print(f"Addition is: {addition(value_one, value_two)}")
elif operation.lower() == "subtraction":
    print(f"Subtraction is: {subtraction(value_one, value_two)}")
elif operation.lower() == "multiplication":
    print(f"Multiplication is: {multiplication(value_one, value_two)}")
elif operation.lower() == "division":
    print(f"Division is: {division(value_one, value_two)}")
elif operation.lower() == "remainder":
    print(f"Remainder is: {remainder(value_one, value_two)}")
else: print(f"Sorry, incorrect operation {operation}")
