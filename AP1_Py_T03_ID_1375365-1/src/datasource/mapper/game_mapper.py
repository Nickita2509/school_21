from domain.model.board import Board
from domain.model.game import Game


class DatasourceGameMapper:
    
    @staticmethod
    def to_domain(data_dict):
        if data_dict is None:
            return None
        
        board = Board(data_dict['board'])
        last_board = Board(data_dict['last_board']) if data_dict.get('last_board') else None
        
        game = Game(game_id=data_dict['game_id'], board=board, last_board=last_board)
        return game
    
    @staticmethod
    def to_datasource(game):
        return game.to_dict()