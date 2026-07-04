# Random dice roller.
import random

def roll_dice():
    random_number = random.randrange(1, 6)
    return random_number



while True:
    print(f"Dice: {roll_dice()}")
    answer = input("Q or q to quit the dice rolling.\nTo continue type anything keys.")
    if answer.lower() == 'q' or answer.lower() == 'Q':
        break