# Email Contact List Sender.

import smtplib

# Sender details.
sender_email = input("Enter your email: ")
password = input("Enter your app password: ")

# Contacts dictionary.
contacts = {
    "Ali": "ali@example.com",
    "Sarah": "sarah@example.com",
}

# Email details.
subject = input("Enter subject: ")
message = input("Enter message: ")

email = f"""Subject: {subject}

{message}
"""

try:
    # Connect to the SMTP server.
    smtp = smtplib.SMTP("smtp.gmail.com", 587)

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, password)

    # Send email to each contact.
    for name, recipient_email in contacts.items():

        smtp.sendmail(sender_email, recipient_email, email)
        print(f"Email sent to {name} ({recipient_email})")

    print("\nAll emails sent successfully!")

except Exception as error:
    print("Error: ", error)

finally:
    smtp.quit()