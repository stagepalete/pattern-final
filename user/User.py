

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