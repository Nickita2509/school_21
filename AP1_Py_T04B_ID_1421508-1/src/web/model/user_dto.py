class UserDTO:
    def __init__(self, user_id=None, login=None):
        self.user_id = user_id
        self.login = login
    
    def to_dict(self):
        return {'user_id': self.user_id, 'login': self.login}