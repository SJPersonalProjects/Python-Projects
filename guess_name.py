# keeps asking the name until the user centers the correct name.

correct_name = "sarim"

while True:
    user_name = input("Guess the name: ")

    if user_name == correct_name:
        print(f"You've guessed. It's {correct_name}")
        break
    else:
        print("It's incorrect. Keep trying.")

