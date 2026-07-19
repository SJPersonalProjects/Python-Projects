# Exception Based Calculator.

print("Simple Calculator.")
print("-" * 30)

try:
    # Get input from the user.
    firstNumber = float(input("Enter first number: "))
    operator = input("Enter an operator (+, -, *, /,): ")
    secondNumber = float(input("Enter the second number: "))

    # Perform the calculation.
    if operator == '+':
        result = firstNumber + secondNumber
    elif operator == '-':
        result = firstNumber - secondNumber
    elif operator == '*':
        result = firstNumber * secondNumber
    elif operator == '/':
        if secondNumber == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = firstNumber / secondNumber
    else:
        raise ValueError("Invalid operator.")
    
    print("Result: ", result)

except ValueError as error:
    print("Error: ", error)

except ZeroDivisionError as error:
    print("Error: ", error)

except Exception as error:
    print("Unexpected Error: ", error)