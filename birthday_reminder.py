# Birthday Reminder.

birthdays = {}

while True:
    print("\n==== Birthday Reminder ====")
    print("1. Add Birthday")
    print("2. Search Birthday")
    print("3. View All Birthdays")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter person's name: ")
        birthday = input("Enter birthday (DD/MM/YYYY): ")

        birthdays[name] = birthday
        print("Birthday added successfully.")
    
    elif choice == '2':
        name = input("Enter person's name to search: ")

        if name in birthdays:
            print(f"{name}'s birthday is {birthdays[name]}")
        else:
            print("Person not found.")
    
    elif choice == '3':
        if len(birthdays) == 0:
            print("No birthdays saved.")
        else:
            print("\nSaved Birthdays:")
            for name in birthdays:
                print(f"{name}: {birthdays[name]}")

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")