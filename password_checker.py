# Password Checker: Checks password with the stored one.

password = "1234*$#1234"

user_password = input("Enter your password: ")

if password == user_password:
    print("Access granted.")
else:
    print("Password is incorrect.")