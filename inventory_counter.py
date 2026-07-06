# Inventory Counter.

inventory = {}

while True:
    print("\n==== Inventory Counter ====")
    print("1. Add Item")
    print("2. Add Stock")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))

        inventory[item] = quantity
        print("Item added.")
    
    elif choice == '2':
        item = input("Enter item name: ")

        if item in inventory:
            quantity = int(input("Enter quantity to add: "))
            inventory[item] += quantity
            print("Stock updated.")
        else:
            print("item not found.")
    
    elif choice == '3':
        if len(inventory) == 0:
            print("No items in inventory")
        else :
            print("\nInventory:")
            for item in inventory:
                print(f"{item} : {inventory[item]}")
    
    elif choice == '4':
        print("Goodbye")
        break

    else :
        print("Invalid option.")