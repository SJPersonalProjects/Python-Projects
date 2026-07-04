# Username formatter: Asks first and last names and combine into fullname.

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

username = first_name.lower() + last_name.lower()

print(f"Your username is: {username}")