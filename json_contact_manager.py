# JSON Contact Manager.

import json
import os

FILENAME = "contacts.json"

# Load contacts.
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
        return []


# Save contacts.
def save_contacts(contacts):
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a contact.
def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# View contacts.
def view_contacts(contacts):
    
    if not contacts:
        print("No contacts found.")
        return

    print("\nContacts")
    print("-" * 30)

    for contact in contacts:
        print(f"Name : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
        print("-" * 30)


# Search contact.
def search_contact(contacts):
    name = input("Error name to search: ").lower()

    found = False

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact Found")
            print(f"Name    :   {contact['name']}")
            print(f"Phone   :   {contact['phone']}")
            print(f"Email   :   {contact['email']}")
            found = True

    if not found:
        print("Contact not found.")


# Main program.
contacts = load_contacts()

while True:

    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contact(contacts)
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid option.")
