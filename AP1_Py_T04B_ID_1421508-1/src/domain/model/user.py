import uuid


class User:
    def __init__(self, user_id=None, login=None, password_hash=None):
        self.user_id = user_id or str(uuid.uuid4())
        self.login = login
        self.password_hash = password_hash