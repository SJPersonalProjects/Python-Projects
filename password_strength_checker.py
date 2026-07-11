# Password Strength Checker.
# Validate a password using a regular expressions.

import re

password = input("Enter a password: ")

length = len(password) >= 8
uppercase = re.search(r"[A-Z]", password)
lowercase = re.search(r"[a-z]", password)
digit = re.search(r"\d", password)

special_pattern = r"[!@#$%^&*(),.?\":{}|<>]"
special = re.search(special_pattern, password)

# Validate the password.
if length and uppercase and lowercase and digit and special:
    print("Strong Password.")
else:
    print("Weak Password")
    print("\nYour password must contain.")

    if not length:
        print(" - At least 8 characters.")
    
    if not uppercase:
        print(" - At least one uppercase letter.")

    if not lowercase:
        print(" - At least one lowercase letter.")

    if not digit:
        print(" - At least one digit.")

    if not special:
        print(" - At least one special character.")