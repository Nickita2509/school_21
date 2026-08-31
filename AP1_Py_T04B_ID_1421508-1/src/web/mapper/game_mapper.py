from domain.model.board import Board
from domain.model.game import Game
from domain.model.game_state import GameState
from web.model.game_dto import GameDTO


class WebGameMapper:
    @staticmethod
    def to_dto(game):
        return GameDTO(
            game_id=game.game_id,
            board=game.board.to_list(),
            state=game.state.value,
            player_x_id=game.player_x_id,
            player_o_id=game.player_o_id,
            current_turn=game.current_turn,
            game_type=game.game_type
        )