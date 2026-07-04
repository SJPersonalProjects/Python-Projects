# Function that returns max number between two values.

def max_number_finder(value_one, value_two):
    max_value = 0
    if value_one > value_two :
        max_value = value_one
    else:
        max_value = value_two
    return max_value


value_one = int(input("Enter value one: "))
value_two = int(input("Enter value two: "))

print(f"Value 1: {value_one}")
print(f"Value 2: {value_two}")
print(f"Greater is: {max_number_finder(value_one, value_two)}")