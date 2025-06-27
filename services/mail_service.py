from models.email import EmailModel
from models.contact import ContactModel
import re
import os

class MailService:
    def __init__(self):
        self.email_model = EmailModel()
        self.contact_model = ContactModel()

    def send_email(self, sender, recipient, subject, body):
        if not recipient.endswith("@gamma.com"):
            recipient += "@gamma.com"
            
        is_contact = recipient in self.contact_model.get_contacts(sender)
        folder = "inbox" if is_contact else "uncontact"
        
        email = self.email_model.create_email(sender, recipient, subject, body, folder)
        return email is not None

    def get_emails(self, username, folder=None):
        return self.email_model.get_emails(username, folder)

    def mark_as_read(self, username, email_id):
        return self.email_model.mark_as_read(username, email_id)

    def export_to_txt(self, email, filename=None):
        if not filename:
            safe_subject = re.sub(r'[^\w\s-]', '', email["subject"]).strip()
            safe_subject = re.sub(r'[-\s]+', '_', safe_subject)
            filename = f"email_{safe_subject[:50]}_{email['id']}.txt"
        
        content = f"From: {email['sender']}\n"
        content += f"To: {email['recipient']}\n"
        content += f"Date: {email['timestamp']}\n"
        content += f"Subject: {email['subject']}\n\n"
        content += email['body']
        
        folder_path = "email_to_text"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'w') as f:
            f.write(content)
        
        return file_path