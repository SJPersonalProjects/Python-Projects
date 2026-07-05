# Number Collector: Collects numbers in a list a print sum, min, max.

# Empty list.
numbers_list = []


while True:
    user_input = input("Enter number to add to list (q to quit): ")
    if user_input.lower() == 'q':
        break
    else:
        numbers_list.append(int(user_input))


sum_value = 0
minimum_value = numbers_list[0]
maximum_value = numbers_list[0]
for i in numbers_list:
    sum_value += i
    if i < minimum_value:
        minimum_value = i
    
    if i > maximum_value:
        maximum_value = i

print(f"Sum: {sum_value}")
print(f"Minimum: {minimum_value}")
print(f"Maximum: {maximum_value}")
