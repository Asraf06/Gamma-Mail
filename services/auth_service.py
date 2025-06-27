from models.user import UserModel
from models.contact import ContactModel

class AuthService:
    def __init__(self):
        self.user_model = UserModel()
        self.contact_model = ContactModel()

    def register(self, username, password):
        if not username.endswith("@gamma.com"):
            username += "@gamma.com"
            
        if self.user_model.create_user(username, password):
            self.contact_model.initialize_user(username)
            return username
        return None

    def login(self, username, password):
        if not username.endswith("@gamma.com"):
            username += "@gamma.com"
            
        if self.user_model.authenticate(username, password):
            return username
        return None