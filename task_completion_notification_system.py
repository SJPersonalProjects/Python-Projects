import os
import shutil
import smtplib
import time

# Perform backup task.
def create_backup(source, destination):
    print("Backup started...")

    # Create destination folder if it doesn't exist.
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Copy files.
    for filename in os.listdir(source):

        source_file = os.path.join(source, filename)
        destination_file = os.path.join(destination, filename)

        if os.path.isfile(source_file):
            shutil.copy(source_file, destination_file)

            print(f"Copied: {filename}")

            # Simulate a long task.
            time.sleep(2)

    print("Backup completed!")


# Send notification email.
def send_notification(sender, password, recipient):

    email = """Subject: Backup Completed
    
Your backup task has finished successfully.
"""

    smtp = smtplib.SMTP(
        "smtp.gmail.com", 587
    )

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(
        sender,
        password
    )

    smtp.sendmail(
        sender,
        recipient,
        email
    )

    smtp.quit()

    print("Notification email sent!")


# Main program.

source_folder = input("Source folder: ")
backup_folder = input("Backup folder: ")

sender_email = input("Your email: ")
password = input("Your app password: ")
recipient_email = input("Send notification to: ")

# run task.
create_backup(
    source_folder,
    backup_folder
)

# Notify when finished.
send_notification(
    sender_email,
    password,
    recipient_email
)