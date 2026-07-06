# Quiz Score Tracker

scores = {}

while True:
    print("\n==== Quiz Score Tracker ====")
    print("1. Add Player")
    print("2. Update Score")
    print("3. View Scores")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        player = input("Enter player name: ")
        scores[player] = 0
        print("Player Added.")

    elif choice == '2':
        player = input("Enter player name: ")

        if player in scores:
            points = int(input("Enter points earned this round: "))
            scores[player] += points
            print(f"Player {player}'s Score updated.")
        
        else:
            print("Player not found.")

    elif choice == '3':

        if len(scores) == 0:
            print("No players added.")
        
        else:
            print("\nScores:")
            for player in scores:
                print(f"{player}: {scores[player]}")

    elif choice == '4':
        print("Goodbye")
        break

    else:
        print("Invalid option.")
        