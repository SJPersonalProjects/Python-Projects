# Function creates and returns sum.

def addition(value_one, value_two):
    return value_one + value_two


value_one = int(input("Enter value one: "))
value_two = int(input("Enter value two: "))

print(f"Total is: {addition(value_one, value_two)}")