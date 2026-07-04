# Login System: Asks login credentials until correct.

stored_username = "sarimjokhio"
stored_password = "password123"


while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == stored_username and password == stored_password:
        print("Access granted")
        break
    elif username == stored_username and password != stored_password:
        print("Password is incorrect")
        continue
    elif username != stored_username and password == stored_password:
        print("Username isn't correct")
        continue
    else:
        print("Username and Password are incorrect.")
        continue
