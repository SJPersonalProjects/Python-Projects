# Automated File Report Emailer.

import os
import smtplib
from datetime import datetime

# Create file report.
def generate_report(folder):

    files = []
    for filename in os.listdir(folder):

        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):

            file_info = {
                "name": filename,
                "size": os.path.getsize(filepath),
                "extension": os.path.splitext(filename)[1]
            }

            files.append(file_info)

    return files

# Save report to text file.
def save_report(files):

    with open("file_report.txt", "w") as file:

        file.write("File Report\n")
        file.write("=" * 40 + "\n")
        file.write(
            f"Created: {datetime.now()}\n\n"
        )

        for item in files:
            file.write(f"Name: {item['name']}\n")
            file.write(f"Size: {item['size']} bytes\n")
            file.write(f"Extension: {item['extension']}\n")
            file.write("-" * 40 + "\n")


# Send email.
def send_email(sender, password, recipient):

    with open("file_report.txt", "r") as file:
        report = file.read()

    email = f"""Subject: Automated File Report
    
{report}    
"""
    
    smtp = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(sender, password)

    smtp.sendmail(
        sender,
        recipient,
        email
    )

    smtp.quit()

# Main Program.
folder = input("Enter folder path: ")

sender_email = input("Your email: ")
password = input("Your app password: ")
recipient_email = input("Send report to: ")

files = generate_report(folder)

save_report(files)

print("Report created successfully!")

send_email(
    sender_email,
    password,
    recipient_email
)

print("Report emailed successfully!")
