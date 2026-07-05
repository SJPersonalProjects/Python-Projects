# Phone Book.

phone_book = {
    "alex": "+11237583835",
    "marry": "+1573857383",
    "chad": "+1535382715",
}


user_search = input("Enter name to fetch phone number: ")

if user_search in phone_book:
    print(f"{user_search}'s phone: {phone_book[user_search]}")
else :
    print("Contact doesn't exist.")