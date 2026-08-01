# Automated Birthday Email Sender.

import smtplib
from datetime import datetime

# Sender details.
sender_email = input("Enter your email: ")
password = input("Enter your app password: ")

# Birthday dictionary.
# Format: "MM-DD"

birthday = {
    "Ali": {
        "email": "ali@example.com",
        "birthday": "08-01"
    },
    "Sara": {
        "email": "sara@example.com",
        "birthday": "12-15"
    },
    "Ahmed": {
        "email": "ahmed@example.com",
        "birthday": "08-01"
    }
}

# Get today's date.
today = datetime.now().strftime("%m-%d")

smtp = None

try:
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender_email, password)

    # Check every birthday.
    for name, details in birthday.items():

        if details["birthday"] == today:

            subject = "Happy Birthday!"

            message = f"""Subject: {subject}

Dear {name},

Wishing you a very Happy Birthday!
Have a wonderful day!

Best wishes
"""
            
            smtp.sendmail(
                sender_email,
                details["email"],
                message
            )

            print(f"Birthday email sent to {name}")

except Exception as error:
    print("Error: ", error)

finally:
    if smtp:
        smtp.quit()