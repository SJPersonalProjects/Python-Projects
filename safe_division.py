# Safe Division: handles divide by zero.

def division(value_one, value_two):
    answer = None
    try:
        answer = value_one / value_two
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    
    return answer


value_one = float(input("Enter value 1: "))
value_two = float(input("Enter value 2: "))

print(f"Division: {division(value_one, value_two)}")