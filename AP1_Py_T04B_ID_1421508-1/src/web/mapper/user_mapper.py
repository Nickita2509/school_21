from domain.model.user import User
from web.model.user_dto import UserDTO


class WebUserMapper:
    @staticmethod
    def to_dto(user):
        return UserDTO(user_id=user.user_id, login=user.login)