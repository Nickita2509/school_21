from domain.model.board import Board
from domain.model.game import Game
from web.model.game_dto import GameDTO


class WebGameMapper:
    
    @staticmethod
    def to_dto(game):
        return GameDTO(
            game_id=game.game_id,
            board=game.board.to_list()
        )
    
    @staticmethod
    def to_domain(dto, existing_game=None):
        if existing_game:
            existing_game.last_board = existing_game.board.copy()
            existing_game.board = Board(dto.board)
            return existing_game
        else:
            return Game(
                game_id=dto.game_id,
                board=Board(dto.board)
            )