class SignUpRequest:
    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password
    
    @staticmethod
    def from_dict(data):
        return SignUpRequest(login=data.get('login'), password=data.get('password'))