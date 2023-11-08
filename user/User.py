import json

class User:
    def __init__(self, username, password, isAdmin, message):
        self.username = username
        self.password = password
        self.is_admin = isAdmin
        self.message = message
    def authenticate(self, entered_password):
        return self.password == entered_password

    def isAdmin(self):
        return self.is_admin
    
    def update(self):
        print(f"Message received: {self.message}")

        with open('data/users.json', 'r') as json_file:
            users = json.load(json_file)

        for user in users:
            if user['username'] == self.username:
                self.message = user['message']

        with open('data/users.json', 'w') as json_file:
            json.dump(users, json_file)
    def __str__(self):
        return f"{self.username}"