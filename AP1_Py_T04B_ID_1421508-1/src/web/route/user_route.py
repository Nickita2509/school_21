from flask import Blueprint, jsonify
from web.mapper.user_mapper import WebUserMapper


user_bp = Blueprint('user', __name__)


class UserController:
    def __init__(self, user_service, authenticator):
        self.user_service = user_service
        self.authenticator = authenticator
    
    def get_user(self, user_id):
        user = self.user_service.get_user_by_id(user_id)
        if user is None:
            return jsonify({'error': 'Пользователь не найден'}), 404
        return jsonify(WebUserMapper.to_dto(user).to_dict()), 200


def register_user_routes(app, user_service, authenticator):
    controller = UserController(user_service, authenticator)
    
    @user_bp.route('/users/<user_id>', methods=['GET'])
    @authenticator.require_auth
    def get_user(user_id):
        return controller.get_user(user_id)
    
    app.register_blueprint(user_bp)