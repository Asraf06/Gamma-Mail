def display_menu():
    print("\n🌟 Gamma Mail Menu 🌟")
    print("1. 📥 Inbox")
    print("2. 🆕 Uncontact")
    print("3. ✉️ Compose Email")
    print("4. 👥 Contacts")
    print("5. 🔍 Search Users")
    print("6. 📤 Export Email to TXT")
    print("7. 🚪 Logout")
    return input("Choose an option: ")

def display_contacts_menu():
    print("\n👥 Contacts Menu 👥")
    print("1. 📋 View Contacts")
    print("2. 📩 View Pending Requests")
    print("3. 🔍 Search User to Add")
    print("4. ↩️ Back to Main Menu")
    return input("Choose an option: ")

def print_emails(emails, folder_name):
    print(f"\n{folder_name} ({len(emails)} emails)")
    for idx, email in enumerate(emails, 1):
        status = "✓" if email["read"] else "✗"
        print(f"{idx}. {status} From: {email['sender']} - {email['subject']} ({email['timestamp']})")

def print_email_details(email):
    print(f"\nFrom: {email['sender']}")
    print(f"Date: {email['timestamp']}")
    print(f"Subject: {email['subject']}")
    print(f"\n{email['body']}")