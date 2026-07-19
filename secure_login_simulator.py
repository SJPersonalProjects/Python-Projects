# Secure Login Simulator.

# Stored Credentials.
correctUsername = "admin"
correctPassword = "python123"

attempts = 3

while attempts > 0:

    try:
        username = input("Username: ")
        password = input("Password: ")

        # Internal assumptions.
        assert attempts >= 0

        # Validates user input
        if username == "":
            raise ValueError("Username cannot be empty.")
        
        if password == "":
            raise ValueError("Password cannot be empty.")

        # Checks credentials.
        if username == correctUsername and password == correctPassword:
            print("\nLogin successful!")
            break

        else:
            attempts -= 1
            print("\nIncorrect username or password.")
            print("Attempts remaining: ", attempts)
    
    except ValueError as error:
        print("Error: ", error)
    
    except AssertionError:
        print("Assertion failed.")

    except Exception as error:
        print("Unexpected Error: ", error)

if attempts == 0:
    print("\nAccount locked.")