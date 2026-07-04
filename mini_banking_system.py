# Mini Banking System.

balance = 1000.0

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient Balance.")
        return balance
    return balance - amount

def check_balance(balance):
    print(f"Current balance: {balance}")


while True:
    print("\n====== Mini Banking System ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    try:
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Amount must be greater than 0")
                continue
            balance = deposit(balance, amount)
            print("Deposit successful.")
        elif choice == "2":
            amount = float(input("Enter withdraw amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            balance = withdraw(balance, amount)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Thank y0ou for using the banking system.")
            break
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")