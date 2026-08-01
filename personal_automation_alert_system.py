# Personal Automation Alert System.

import os
import shutil
import smtplib
from datetime import datetime
from twilio.rest import Client

# Store alert information.
alerts = []

# Check missing files.
def check_missing_file(filename):

    if not os.path.exists(filename):

        alerts.append({
            "type": "Missing File",
            "message": f"{filename} was not found."
        })


# Check disk space.
def check_disk_space():

    total, used, free = shutil.disk_usage("/")

    free_gb = free / {1024 ** 3}

    if free_gb < 5:

        alerts.append({
            "type": "Low Disk Space",
            "message": f"Only {free_gb:.2f} GB remaining"
        })


# Simulate failed login detection.
def check_failed_login(attempts):

    if attempts > 5:
        alerts.append({
            "type": "Security Alert",
            "message": f"{attempts} failed login attempts detected."
        })


# Send email alert.
def send_email_alert(sender, password, recipient):

    if not alerts:
        return
    
    message = "Automation Alerts\n\n"

    for alert in alerts:
        message += (
            f"{alert['type']}\n"
            f"{alert['message']}\n\n"
        )

    email = f"""Subject: Automation Alert
    
{message}

Time: {datetime.now()}
"""
    
    smtp = smtplib.SMTP(
        "smtp.gmail.com",
        587
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


# Send SMS alert.
def send_sms_alert():

    if not alerts:
        return
    
    account_sid = "YOUR_ACCOUNT_SID"
    auth_token = "YOUR_AUTH_TOKEN"

    client = Client(
        account_sid,
        auth_token
    )

    message = client.message.create(
        body="Automation alert detected. Check email for details.",
        from_="YOUR_TWILIO_NUMBER",
        to="YOUR_PHONE_NUMBER"
    )

    print("SMS sent!")

# Main program.
check_missing_file("important_backup.zip")

check_disk_space()

# Example failed login count.
check_failed_login(7)

if alerts:
    print("Alerts detected:")

    for alert in alerts:
        print(
            alert["type"],
            "-",
            alert["message"]
        )

    sender = input("Your email: ")
    password = input("App password: ")
    recipient = input("Send alert to: ")

    send_email_alert(
        sender,
        password,
        recipient
    )

    send_sms_alert()

    print("\nNotification sent!")

else:
    print("No problems detected.")