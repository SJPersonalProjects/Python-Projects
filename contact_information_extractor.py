# Contact Information Extractor
# Extract all phone numbers and emails addresses
# Remove duplicates, and display the results.

import re

# Ask teh user to enter a paragraph.
text = input("Enter a paragraph:\n")

# Regular expression for phone numbers.
phone_pattern = r"\d{3}-\d{3}-\d{4}"

# Regular expression for email addresses.
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all phone numbers.
phone = re.findall(phone_pattern, text)

# Find all the email addresses.
email = re.findall(email_pattern, text)

# Remove duplicates.
phones = sorted(set(phone))
emails = sorted(set(email))

# Display phone numbers.
print("\nPhone Numbers")
print("-" * 30)

if phones:
    for phoneNumber in phones:
        print(phoneNumber)

else:
    print("No phone numbers found.")


# Display email addresses.
print("\nEmail Addresses")
print("-" * 30)

if emails:
    for emailAddress in emails:
        print(emailAddress)

else:
    print("No email addresses found.")


# Save the results to a file.
with open("contacts.txt", "w") as file:
    file.write("Phone Numbers\n")
    file.write("-" * 30 + "\n")

    if phones:
        for phoneNumber in phones:
            file.write(phoneNumber + "\n")
        else:
            file.write("No phone numbers found.\n")
    
    file.write("\nEmail Addresses\n")
    file.write("-" * 30 + "\n")

    if emails:
        for emailAddress in emails:
            file.write(emailAddress + "\n")

    else:
        file.write("No email addresses found.\n")

print("\nResults have been saved to contacts.txt")