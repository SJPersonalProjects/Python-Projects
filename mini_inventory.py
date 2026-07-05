# Mini Inventory List version.

inventory = []

while True:
    print("\n==== Mini Inventory ====")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        product = input("Enter product name: ")

        if product not in inventory:
            inventory.append(product)
            print("Product added successfully.")
        else:
            print("Product already exists.")
    
    
    elif choice == '2':
        product = input("Enter product name to remove: ")

        if product in inventory:
            inventory.remove(product)
            print("Product removed successfully.")
        else:
            print("Product not found.")
    
    
    elif choice == '3':
        if len(inventory) == '0':
            print("Inventory is empty.")
        else:
            print("\nProducts in Inventory:")
            for product in inventory:
                print(product)
    
    
    elif choice == '4':
        print("Exiting inventory system.")
        break


    else:
        print("Invalid option. Please try again.")