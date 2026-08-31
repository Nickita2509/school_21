from domain.model.user import User
from datasource.model.user_model import UserModel


class UserMapper:
    model_class = UserModel
    
    def to_domain(self, model):
        if model is None:
            return None
        return User(user_id=model.id, login=model.login, password_hash=model.password_hash)
    
    def to_model(self, user):
        if user is None:
            return None
        return UserModel(id=user.user_id, login=user.login, password_hash=user.password_hash)