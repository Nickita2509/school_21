import base64
from werkzeug.security import check_password_hash
from domain.service.auth_service import AuthService
from domain.service.user_service import UserService


class AuthServiceImpl(AuthService):
    def __init__(self, user_service):
        self.user_service = user_service
    
    def signup(self, login, password):
        if not login or not password:
            raise ValueError("Логин и пароль обязательны")
        if len(login) < 3 or len(password) < 3:
            raise ValueError("Логин и пароль должны быть не короче 3 символов")
        
        user = self.user_service.create_user(login, password)
        return user.user_id
    
    def login(self, auth_header):
        if not auth_header or not auth_header.startswith('Basic '):
            raise ValueError("Неверный формат авторизации")
        
        try:
            encoded = auth_header.split(' ')[1]
            decoded = base64.b64decode(encoded).decode('utf-8')
            login, password = decoded.split(':', 1)
        except Exception:
            raise ValueError("Неверный формат авторизации")
        
        user = self.user_service.get_user_by_login(login)
        if user is None:
            raise ValueError("Неверный логин или пароль")
        
        if not check_password_hash(user.password_hash, password):
            raise ValueError("Неверный логин или пароль")
        
        return user.user_id