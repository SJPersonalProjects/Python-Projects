# Email Reader Extractor.

import imapclient
import pyzmail

# Email account.
email = input("Enter your email: ")
password = input("Enter your app password: ")

# Connect to Gmail
imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login(email, password)

# Open inbox.
imap.select_folder("INBOX", readonly=True)

# Get the latest 5 emails.
uids = imap.search(["ALL"])
latest_uids = uids[-5:]

# open output file.
with open("emails.txt", "w", encoding="utf-8") as file:

    for uid in latest_uids:

        raw_message = imap.fetch([uid], ["BODY[]"])

        message = pyzmail.PyzMessage.factory(
            raw_message[uid][b"BODY[]"]
        )

        sender = message.get_addresses("from")
        subject = message.get_subject()

        # Get the message body.
        if message.text_part:
            body = message.text_part.get_payload().decode(
                message.text_part.charset
            )
        else:
            body = "No text body found."

        
        # Save to file.
        file.write(f"UID: {uid}\n")
        file.write(f"From: {sender}\n")
        file.write(f"Subject: {subject}\n")
        file.write("Message:\n")
        file.write(body)
        file.write("-" * 50)
        file.write("\n")

print("Emails saved to emails.txt")
imap.logout()