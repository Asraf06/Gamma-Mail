import json
import os

class UserModel:
    def __init__(self, db_file="database/users.json"):
        self.db_file = db_file
        self._initialize_db()

    def _initialize_db(self):
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as f:
                json.dump({}, f)

    def create_user(self, username, password):
        with open(self.db_file, 'r') as f:
            users = json.load(f)
            
        if username in users:
            return False
            
        users[username] = {"password": password}
        
        with open(self.db_file, 'w') as f:
            json.dump(users, f, indent=4)
        return True

    def authenticate(self, username, password):
        with open(self.db_file, 'r') as f:
            users = json.load(f)
            
        if username not in users or users[username]["password"] != password:
            return False
        return True

    def user_exists(self, username):
        with open(self.db_file, 'r') as f:
            users = json.load(f)
        return username in users