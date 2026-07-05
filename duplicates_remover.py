# Removes duplicate values from a list.

numbers_list = [1, 2, 5, 2, 3, 4, 1, 2, 3, 7, 8, 9, 16, 11]
unique_numbers = []

for i in numbers_list:
    if i not in unique_numbers:
        unique_numbers.append(i)


print(f"\nOriginal List:{numbers_list}")
print(f"Unique List: {unique_numbers}")