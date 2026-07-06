# Email Checker.

email = input("Enter your email: ")

if email.startswith("@"):
    print("Email cannot start with '@'.")
elif not email.endswith(".com"):
    print("Emails must end with '.com'.")
elif "@" not in email:
    print("Email must contain '@'.")
else:
    print("Email is valid.")