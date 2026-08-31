from domain.model.board import Board
from domain.model.game import Game
from domain.model.game_state import GameState
from datasource.model.game_model import GameModel


class GameMapper:
    model_class = GameModel
    
    def to_domain(self, model):
        if model is None:
            return None
        return Game(
            game_id=model.id,
            board=Board(model.board),
            state=GameState(model.state),
            player_x_id=model.player_x_id,
            player_o_id=model.player_o_id,
            current_turn=int(model.current_turn) if model.current_turn is not None else None,
            game_type=model.game_type,
            last_board=Board(model.last_board) if model.last_board else None
        )
    
    def to_model(self, game):
        if game is None:
            return None
        return GameModel(
            id=game.game_id,
            board=game.board.to_list(),
            state=game.state.value,
            player_x_id=game.player_x_id,
            player_o_id=game.player_o_id,
            current_turn=game.current_turn,
            game_type=game.game_type,
            last_board=game.last_board.to_list() if game.last_board else None
        )