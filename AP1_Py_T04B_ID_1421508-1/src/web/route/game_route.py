from flask import Blueprint, request, jsonify
from web.mapper.game_mapper import WebGameMapper


game_bp = Blueprint('game', __name__)


class GameController:
    def __init__(self, game_service, authenticator):
        self.game_service = game_service
        self.authenticator = authenticator
    
    def create_game(self):
        try:
            data = request.get_json() or {}
            game_type = data.get('game_type', 'pvp')
            user_id = request.current_user_id
            game = self.game_service.create_game(user_id, game_type)
            return jsonify(WebGameMapper.to_dto(game).to_dict()), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    
    def get_games(self):
        games = self.game_service.get_available_games()
        return jsonify([WebGameMapper.to_dto(g).to_dict() for g in games]), 200
    
    def join_game(self, game_id):
        try:
            user_id = request.current_user_id
            game = self.game_service.join_game(game_id, user_id)
            return jsonify(WebGameMapper.to_dto(game).to_dict()), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    
    def make_move(self, game_id):
        try:
            data = request.get_json()
            if not data or 'board' not in data:
                return jsonify({'error': 'Необходимо передать поле board'}), 400
            
            user_id = request.current_user_id
            game = self.game_service.make_move(game_id, user_id, data['board'])
            return jsonify(WebGameMapper.to_dto(game).to_dict()), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    
    def get_game(self, game_id):
        game = self.game_service.get_game(game_id)
        if game is None:
            return jsonify({'error': 'Игра не найдена'}), 404
        return jsonify(WebGameMapper.to_dto(game).to_dict()), 200


def register_game_routes(app, game_service, authenticator):
    controller = GameController(game_service, authenticator)
    
    @game_bp.route('/games', methods=['POST'])
    @authenticator.require_auth
    def create_game():
        return controller.create_game()
    
    @game_bp.route('/games', methods=['GET'])
    @authenticator.require_auth
    def get_games():
        return controller.get_games()
    
    @game_bp.route('/games/<game_id>/join', methods=['POST'])
    @authenticator.require_auth
    def join_game(game_id):
        return controller.join_game(game_id)
    
    @game_bp.route('/games/<game_id>/move', methods=['POST'])
    @authenticator.require_auth
    def make_move(game_id):
        return controller.make_move(game_id)
    
    @game_bp.route('/games/<game_id>', methods=['GET'])
    @authenticator.require_auth
    def get_game(game_id):
        return controller.get_game(game_id)
    
    app.register_blueprint(game_bp)