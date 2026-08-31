from flask import Blueprint, request, jsonify
from web.model.auth_dto import SignUpRequest


auth_bp = Blueprint('auth', __name__)


class AuthController:
    def __init__(self, auth_service):
        self.auth_service = auth_service
    
    def signup(self):
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Тело запроса должно быть JSON'}), 400
            
            req = SignUpRequest.from_dict(data)
            user_id = self.auth_service.signup(req.login, req.password)
            return jsonify({'user_id': user_id, 'message': 'Регистрация успешна'}), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    
    def login(self):
        try:
            auth_header = request.headers.get('Authorization')
            user_id = self.auth_service.login(auth_header)
            return jsonify({'user_id': user_id, 'message': 'Авторизация успешна'}), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 401


def register_auth_routes(app, auth_service, authenticator):
    controller = AuthController(auth_service)
    
    @auth_bp.route('/signup', methods=['POST'])
    def signup():
        return controller.signup()
    
    @auth_bp.route('/login', methods=['POST'])
    def login():
        return controller.login()
    
    app.register_blueprint(auth_bp)