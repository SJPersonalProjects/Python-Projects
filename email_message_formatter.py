# Email Message Formatter.

# Ask the user for email details.
recipient = input("Recipient Name: ")
subject = input("Subject: ")


print("Ente ryour message: ")
message = input()

# Display the formatted email.
print("\n" + "=" * 50)
print("To: ", recipient)
print("Subject: ", subject)
print()

print(f"Dear {recipient}")
print()

print(message)
print()

print("Best regards,")
print("Your Name")
print("=" * 50)