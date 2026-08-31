class UserService:
    def create_user(self, login, password):
        raise NotImplementedError
    
    def get_user_by_login(self, login):
        raise NotImplementedError
    
    def get_user_by_id(self, user_id):
        raise NotImplementedError