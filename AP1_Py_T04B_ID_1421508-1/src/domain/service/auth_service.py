class AuthService:
    def signup(self, login, password):
        raise NotImplementedError
    
    def login(self, auth_header):
        raise NotImplementedError