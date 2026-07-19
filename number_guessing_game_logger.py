# Number Guessing Game Logger.

import random
import logging

# Configure logging.
logging.basicConfig(
    filename="GuessGame.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("==== Number Guessing Game ====")

secretNumber = random.randint(1, 20)
attempts = 0

logging.info("New game started.")
logging.debug(f"Secret number generated: {secretNumber}")

while True:

    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    logging.info(f"Attempt {attempts}: User guessed {guess}")

    if guess < secretNumber:
        print("Too low!")
        logging.debug("Guess was too low.")

    elif guess > secretNumber:
        print("Too high!")
        logging.debug("Guess was too high.")

    else:
        print("Congratulations! You guessed the number.")
        print("Attempts: ", attempts)

        logging.info("User guessed the correct number.")
        logging.info(f"Game finished in {attempts} attempts.")
        break