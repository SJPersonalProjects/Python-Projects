# Simple Email Sender.

import smtplib

# Sender details.
sender_email = input("Enter your email: ")
password = input("Enter your app Password: ")

# Recipient details.
recipient_email = input("Enter recipient email: ")
subject = input("Enter subject: ")
message = input("Enter message: ")

# Create email.
email = f"""Subject: {subject}

{message}
"""

try:
    # Connect to the SMTP server.
    smtp = smtplib.SMTP("smtp.gmail.com", 587)

    # Identify outselves to the server.
    smtp.ehlo()

    # Start encrypted connection.
    smtp.starttls()

    # Identify ourselves again after encryption.
    smtp.ehlo()

    # Log in.
    smtp.login(sender_email, password)

    # Send the email.
    smtp.sendmail(sender_email, recipient_email, email)

    print("Email sent successfully!")

except Exception as error:
    print("Error: ", error)

finally:
    smtp.quit()