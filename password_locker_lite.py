# Password Locker Lite

passwords = {
    "gmail": "gmail123",
    "facebook": "fb@123",
    "github": "git456"
}

def get_password(account):
    if account in passwords:
        return passwords[account]
    else:
        return None
    

while True:
    account = input("Enter account name (q to quit): ")

    if account.lower() == 'q':
        break

    password = get_password(account)

    if password:
        print(f"Password: {password}")
    else:
        print("Account not found.")