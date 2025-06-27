from models.user import UserModel
from models.contact import ContactModel
from models.email import EmailModel
import json

class ContactService:
    def __init__(self):
        self.user_model = UserModel()
        self.contact_model = ContactModel()
        self.email_model = EmailModel()

    def search_users(self, query):
        with open(self.user_model.db_file, 'r') as f:
            users = json.load(f)
        return [user for user in users.keys() if query.lower() in user.lower()]

    def send_request(self, sender, recipient):
        if not recipient.endswith("@gamma.com"):
            recipient += "@gamma.com"
            
        if not self.user_model.user_exists(recipient):
            return False
            
        if recipient in self.contact_model.get_contacts(sender):
            return False
            
        if recipient in self.contact_model.get_sent_requests(sender):
            return False
            
        return self.contact_model.add_request(sender, recipient)

    def respond_request(self, user, requester, accept):
        if requester not in self.contact_model.get_pending_requests(user):
            return False
            
        self.contact_model.remove_request(requester, user)
        
        if accept:
            self.contact_model.add_contact(user, requester)
            self.email_model.move_to_inbox(requester, user)
        
        return True

    def get_contacts(self, username):
        return self.contact_model.get_contacts(username)

    def get_pending_requests(self, username):
        return self.contact_model.get_pending_requests(username)

    def get_sent_requests(self, username):
        return self.contact_model.get_sent_requests(username)