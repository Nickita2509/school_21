from werkzeug.security import generate_password_hash
from domain.model.user import User
from domain.service.user_service import UserService


class UserServiceImpl(UserService):
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def create_user(self, login, password):
        if self.user_repository.get_by_login(login):
            raise ValueError("Пользователь с таким логином уже существует")
        
        password_hash = generate_password_hash(password)
        user = User(login=login, password_hash=password_hash)
        self.user_repository.save(user)
        return user
    
    def get_user_by_login(self, login):
        return self.user_repository.get_by_login(login)
    
    def get_user_by_id(self, user_id):
        return self.user_repository.get(user_id)