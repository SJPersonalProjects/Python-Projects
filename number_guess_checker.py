# Number Guess Checker: User finds secret number.

secret_number = 17

user_number = int(input("Geuss the secret number: "))

if secret_number == user_number:
    print(f"You've guessed the secret number. It's {secret_number}")
else:
    print(f"Sorry, it's not the {user_number}")