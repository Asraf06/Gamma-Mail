from services.auth_service import AuthService
from services.mail_service import MailService
from services.contact_service import ContactService
from utils.helpers import (
    display_menu, 
    display_contacts_menu,
    print_emails,
    print_email_details
)

class GammaMailApp:
    def __init__(self):
        self.auth_service = AuthService()
        self.mail_service = MailService()
        self.contact_service = ContactService()
        self.current_user = None

    def run(self):
        while True:
            if not self.current_user:
                self._show_auth_menu()
            else:
                self._show_main_menu()

    def _show_auth_menu(self):
        print("\n🔐 Gamma Mail - Welcome! 🔐")
        print("1. 👤 Login")
        print("2. 📝 Register")
        print("3. 🚪 Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            username = input("Enter your email: ")
            password = input("Enter your password: ")
            self.current_user = self.auth_service.login(username, password)
        elif choice == "2":
            username = input("Choose a username (will end with @gamma.com): ")
            password = input("Choose a password: ")
            self.current_user = self.auth_service.register(username, password)
        elif choice == "3":
            print("👋 Goodbye!")
            exit()
        else:
            print("❌ Invalid option!")

    def _show_main_menu(self):
        choice = display_menu()
        
        if choice == "1":  # Inbox
            self._handle_inbox()
        elif choice == "2":  # Uncontact
            self._handle_uncontact()
        elif choice == "3":  # Compose Email
            self._handle_compose_email()
        elif choice == "4":  # Contacts
            self._handle_contacts()
        elif choice == "5":  # Search Users
            self._handle_search_users()
        elif choice == "6":  # Export Email
            self._handle_export_email()
        elif choice == "7":  # Logout
            print(f"👋 Goodbye, {self.current_user}!")
            self.current_user = None
        else:
            print("❌ Invalid option!")

    def _handle_inbox(self):
        emails = self.mail_service.get_emails(self.current_user, "inbox")
        print_emails(emails, "📥 Inbox")
        self._view_email_details(emails)

    def _handle_uncontact(self):
        emails = self.mail_service.get_emails(self.current_user, "uncontact")
        print_emails(emails, "🆕 Uncontact")
        
        if emails:
            view_email = input("Enter email number to view (or 0 to go back): ")
            if view_email.isdigit() and int(view_email) > 0:
                selected = emails[int(view_email)-1]
                self.mail_service.mark_as_read(self.current_user, selected["id"])
                print_email_details(selected)
                
                add_contact = input(f"\nAdd {selected['sender']} to contacts? (y/n): ").lower()
                if add_contact == "y":
                    self.contact_service.respond_request(self.current_user, selected["sender"], True)

    def _handle_compose_email(self):
        recipient = input("To: ")
        subject = input("Subject: ")
        body = input("Message:\n")
        if self.mail_service.send_email(self.current_user, recipient, subject, body):
            print("✉️ Email sent successfully!")
        else:
            print("❌ Failed to send email!")

    def _handle_contacts(self):
        while True:
            sub_choice = display_contacts_menu()
            
            if sub_choice == "1":  # View Contacts
                contacts = self.contact_service.get_contacts(self.current_user)
                print(f"\n📋 Your Contacts ({len(contacts)})")
                for idx, contact in enumerate(contacts, 1):
                    print(f"{idx}. {contact}")
            
            elif sub_choice == "2":  # Pending Requests
                self._handle_pending_requests()
            
            elif sub_choice == "3":  # Search and Add User
                self._handle_search_add_user()
            
            elif sub_choice == "4":  # Back
                break
            else:
                print("❌ Invalid option!")

    def _handle_pending_requests(self):
        pending = self.contact_service.get_pending_requests(self.current_user)
        print(f"\n📩 Pending Contact Requests ({len(pending)})")
        for idx, requester in enumerate(pending, 1):
            print(f"{idx}. {requester}")
        
        if pending:
            req_choice = input("Enter request number to respond (or 0 to go back): ")
            if req_choice.isdigit() and int(req_choice) > 0:
                selected = pending[int(req_choice)-1]
                action = input(f"Accept contact request from {selected}? (y/n): ").lower()
                if self.contact_service.respond_request(self.current_user, selected, action == "y"):
                    print("✅ Request processed!")
                else:
                    print("❌ Failed to process request!")

    def _handle_search_add_user(self):
        query = input("Enter email to search: ")
        results = self.contact_service.search_users(query)
        
        if not results:
            print("❌ No users found!")
        else:
            print("\n🔍 Search Results:")
            for idx, user in enumerate(results, 1):
                print(f"{idx}. {user}")
            
            add_choice = input("Enter user number to send request (or 0 to go back): ")
            if add_choice.isdigit() and int(add_choice) > 0:
                selected = results[int(add_choice)-1]
                if selected != self.current_user:
                    if self.contact_service.send_request(self.current_user, selected):
                        print("📩 Contact request sent!")
                    else:
                        print("❌ Failed to send request!")
                else:
                    print("❌ You can't add yourself!")

    def _handle_search_users(self):
        query = input("Enter search query: ")
        results = self.contact_service.search_users(query)
        
        if not results:
            print("❌ No users found!")
        else:
            print("\n🔍 Search Results:")
            for idx, user in enumerate(results, 1):
                print(f"{idx}. {user}")

    def _handle_export_email(self):
        folder_choice = input("Export from (1) Inbox or (2) Uncontact? ")
        folder = "inbox" if folder_choice == "1" else "uncontact"
        emails = self.mail_service.get_emails(self.current_user, folder)
        
        if not emails:
            print(f"❌ No emails in {folder}!")
        else:
            print(f"\nEmails in {folder}:")
            for idx, email in enumerate(emails, 1):
                print(f"{idx}. {email['subject']} - {email['timestamp']}")
            
            export_choice = input("Enter email number to export (or 0 to go back): ")
            if export_choice.isdigit() and int(export_choice) > 0:
                selected = emails[int(export_choice)-1]
                filename = self.mail_service.export_to_txt(selected)
                print(f"📄 Email exported to {filename}!")

    def _view_email_details(self, emails):
        if emails:
            view_email = input("Enter email number to view (or 0 to go back): ")
            if view_email.isdigit() and int(view_email) > 0:
                selected = emails[int(view_email)-1]
                self.mail_service.mark_as_read(self.current_user, selected["id"])
                print_email_details(selected)

if __name__ == "__main__":
    app = GammaMailApp()
    app.run()