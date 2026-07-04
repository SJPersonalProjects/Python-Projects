# Number guess game.

import random


def generate_number():
    random_number = random.randint(1, 20)
    return random_number


def check_guess(user_guess, secret_number):
    if user_guess == secret_number:
        print("Congratulations, you've guessed the correct number.")
        return True
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    return False
    


secret_number = generate_number()
print("Random number has been generated.")

while True:
    user_guess = int(input("Enter number to guess the secret number (1 to 20): "))
    if user_guess >= 1 and user_guess <= 20:
        if check_guess(user_guess, secret_number): break
    else:
        print("Sorry, number is incorrect. Range is 1 to 20")