import json
import os
from datetime import datetime

class EmailModel:
    def __init__(self, db_file="database/emails.json"):
        self.db_file = db_file
        self._initialize_db()

    def _initialize_db(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({}, f)

    def create_email(self, sender, recipient, subject, body, folder):
        email = {
            "id": str(datetime.now().timestamp()),
            "sender": sender,
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "read": False,
            "folder": folder
        }
        
        with open(self.db_file, 'r') as f:
            emails = json.load(f)
            
        if recipient not in emails:
            emails[recipient] = []
            
        emails[recipient].append(email)
        
        with open(self.db_file, 'w') as f:
            json.dump(emails, f, indent=4)
        return email

    def get_emails(self, recipient, folder=None):
        with open(self.db_file, 'r') as f:
            emails = json.load(f)
            
        if recipient not in emails:
            return []
            
        if folder:
            return [email for email in emails[recipient] if email["folder"] == folder]
        return emails[recipient]

    def mark_as_read(self, recipient, email_id):
        with open(self.db_file, 'r') as f:
            emails = json.load(f)
            
        if recipient in emails:
            for email in emails[recipient]:
                if email["id"] == email_id:
                    email["read"] = True
                    break
        
        with open(self.db_file, 'w') as f:
            json.dump(emails, f, indent=4)
        return True

    def move_to_inbox(self, sender, recipient):
        with open(self.db_file, 'r') as f:
            emails = json.load(f)
            
        if recipient in emails:
            for email in emails[recipient]:
                if email["sender"] == sender and email["folder"] == "uncontact":
                    email["folder"] = "inbox"
        
        with open(self.db_file, 'w') as f:
            json.dump(emails, f, indent=4)
        return True