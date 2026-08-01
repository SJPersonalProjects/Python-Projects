# Email Inbox Search Tool.

import imapclient
import pyzmail

# Email account.
email = input("Enter your email: ")
password = input("Enter your app password: ")

# Connect to Gmail.
imap = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap.login(email, password)

# Open the Inbox.
imap.select_folder("INBOX", readonly=True)


print("\nSearch Options")
print("1. Unread Emails")
print("2. Emails From Sender")
print("3. Emails By Subject")

choice = input("Choose an option: ")

if choice == "1":
    uids = imap.search(["UNSEEN"])

elif choice == "2":
    sender = input("Enter sender email: ")
    uids = imap.search(["FROM", sender])

elif choice == "3":
    subject = input("Enter subject: ")
    uids = imap.search(["SUBJECT", subject])

else:
    print("Invalid choice.")
    imap.logout()
    exit()


print(f"\nFound {len(uids)} email(s).\n")

# Display email information.
for uid in uids:
    raw_message = imap.fetch([uid], ["BODY[]"])

    message = pyzmail.PyzMessage.factory(
        raw_message[uid][b"BODY[]"]
    )

    print(f"UID         :       {uid}")
    print(f"From        :       {message.get_address('from')}")
    print(f"Subject     :       {message.get_subject()}")
    print("-" * 40)


imap.logout()