# Password Vault Lite.

import os
import logging

# Configure logging
logging.basicConfig(
    filename="VaultLog.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

vaultFile = "PasswordVault.txt"

# Create the vault file if it doesn't exist.
if not os.path.exists(vaultFile):
    open(vaultFile, "w").close()

while True:

    print("\nPassword Vault")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':

        website = input("Website: ")
        password = input("Password: ")

        file = open(vaultFile, "a")
        file.write(website + ":" + password + "\n")
        file.close()

        logging.info(f"Added password for website: {website}")

        print("Password saved.")

    elif choice == '2':
        website = input("Enter website: ")

        try:

            found = False

            file = open(vaultFile, "r")

            for line in file:

                savedWebsite, savedPassword = line.strip().split(":")

                if savedWebsite == website:
                    print("Password: ", savedPassword)

                    logging.info(f"Retrieved password for website: {website}")

                    found = True
                    break

            file.close()

            if not found:
                raise LookupError("Website not found.")
        
        except LookupError as error:
            print(error)
            logging.warning(f"Looking failed for website: {website}")
    
    elif choice == '3':
        logging.info("Vault closed.")
        print("Goodbye!")
        break
    
    else:

        print("Invalid options")
        logging.warning("Invalid menu options selected.")
