# Password Validator

password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True


if len(password) == 0:
    print("Password must be at least 8 characters long.")
elif not has_upper:
    print("Password must contain an uppercase letter.")
elif not has_lower:
    print("Password must contain a lowercase letter.")
elif not has_digit:
    print("Password must contain a digit.")
else:
    print("Password is valid.")