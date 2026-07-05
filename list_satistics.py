# List Satistics

numbers = []


while True:
    user_input = input("Enter a number (q to quit): ")
    
    if user_input.lower() == 'q':
        break

    numbers.append(int(user_input))


even_counter = 0
odd_counter = 0
positive_counter = 0
negative_counter = 0


for number in numbers:
    if number % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
    

    if number > 0:
        positive_counter += 1
    elif number < 0:
        negative_counter += 1

print("\n==== List Satistics ====")
print(f"Even numbers: {even_counter}")
print(f"Odd numbers: {odd_counter}")
print(f"Positive numbers: {positive_counter}")
print(f"Negative numbers: {negative_counter}")