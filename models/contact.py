import json
import os

class ContactModel:
    def __init__(self, db_file="database/contacts.json"):
        self.db_file = db_file
        self._initialize_db()

    def _initialize_db(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({}, f)

    def initialize_user(self, username):
        with open(self.db_file, 'r') as f:
            contacts = json.load(f)
            
        if username not in contacts:
            contacts[username] = {
                "contacts": [],
                "pending_requests": [],
                "sent_requests": []
            }
        
        with open(self.db_file, 'w') as f:
            json.dump(contacts, f, indent=4)
        return True

    def add_contact(self, user1, user2):
        with open(self.db_file, 'r') as f:
            contacts = json.load(f)
            
        if user2 not in contacts[user1]["contacts"]:
            contacts[user1]["contacts"].append(user2)
        if user1 not in contacts[user2]["contacts"]:
            contacts[user2]["contacts"].append(user1)
        
        with open(self.db_file, 'w') as f:
            json.dump(contacts, f, indent=4)
        return True

    def add_request(self, sender, recipient):
        with open(self.db_file, 'r') as f:
            contacts = json.load(f)
            
        if recipient not in contacts[sender]["sent_requests"]:
            contacts[sender]["sent_requests"].append(recipient)
        if sender not in contacts[recipient]["pending_requests"]:
            contacts[recipient]["pending_requests"].append(sender)
        
        with open(self.db_file, 'w') as f:
            json.dump(contacts, f, indent=4)
        return True

    def remove_request(self, sender, recipient):
        with open(self.db_file, 'r') as f:
            contacts = json.load(f)
            
        if recipient in contacts[sender]["sent_requests"]:
            contacts[sender]["sent_requests"].remove(recipient)
        if sender in contacts[recipient]["pending_requests"]:
            contacts[recipient]["pending_requests"].remove(sender)
        
        with open(self.db_file, 'w') as f:
            json.dump(contacts, f, indent=4)
        return True

    def get_contacts(self, username):
        with open(self.db_file, 'r') as f:
            contacts = json.load(f)
        return contacts.get(username, {}).get("contacts", [])

    def get_pending_requests(self, username):
        with open(self.db_file, 'r') as f:
            contacts = json.load(f)
        return contacts.get(username, {}).get("pending_requests", [])

    def get_sent_requests(self, username):
        with open(self.db_file, 'r') as f:
            contacts = json.load(f)
        return contacts.get(username, {}).get("sent_requests", [])