from flask import Blueprint, request, jsonify
from web.model.game_dto import GameDTO
from web.mapper.game_mapper import WebGameMapper
from domain.model.board import Board


game_bp = Blueprint('game', __name__)


class GameController:
    
    def __init__(self, game_service, game_repository):
        self.game_service = game_service
        self.game_repository = game_repository
    
    def process_move(self, game_id):
        try:
            data = request.get_json()
            if not data:
                return jsonify({'error': 'Тело запроса должно быть JSON'}), 400
            
            dto = GameDTO.from_dict(data)
            
            game_data = self.game_repository.get(game_id)
            
            if game_data is None:
                if dto.board is None:
                    return jsonify({'error': 'Для новой игры нужно передать пустое поле'}), 400
                game = WebGameMapper.to_domain(dto)
                game.game_id = game_id
                self.game_repository.save(game)
                
                if all(cell == Board.EMPTY for row in game.board.matrix for cell in row):
                    from web.mapper.game_mapper import WebGameMapper as WMapper
                    return jsonify(WMapper.to_dto(game).to_dict()), 200
            else:
                from datasource.mapper.game_mapper import DatasourceGameMapper
                game = DatasourceGameMapper.to_domain(game_data)

                game.last_board = game.board.copy()

                try:
                    new_board = self.game_service.validate_board(game, dto.board)
                    game.board = new_board
                except ValueError as e:
                    return jsonify({'error': str(e)}), 400

                result = self.game_service.check_game_over(game.board)
                if result == Board.X:
                    self.game_repository.save(game)
                    return jsonify({
                        'game_id': game.game_id,
                        'board': game.board.to_list(),
                        'status': 'player_wins'
                    }), 200
                elif result == 'draw':
                    self.game_repository.save(game)
                    return jsonify({
                        'game_id': game.game_id,
                        'board': game.board.to_list(),
                        'status': 'draw'
                    }), 200
                
                game = self.game_service.get_next_move(game)
                
                result = self.game_service.check_game_over(game.board)
                status = 'playing'
                if result == Board.O:
                    status = 'computer_wins'
                elif result == 'draw':
                    status = 'draw'
                
                from web.mapper.game_mapper import WebGameMapper as WMapper
                response = WMapper.to_dto(game).to_dict()
                response['status'] = status
                return jsonify(response), 200

            from web.mapper.game_mapper import WebGameMapper as WMapper
            return jsonify(WMapper.to_dto(game).to_dict()), 200
            
        except Exception as e:
            return jsonify({'error': f'Внутренняя ошибка: {str(e)}'}), 500


def register_routes(app, game_service, game_repository):

    controller = GameController(game_service, game_repository)
    
    @game_bp.route('/game/<game_id>', methods=['POST'])
    def process_move(game_id):
        return controller.process_move(game_id)
    
    app.register_blueprint(game_bp)