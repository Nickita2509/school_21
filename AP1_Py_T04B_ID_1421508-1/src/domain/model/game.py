import uuid
from domain.model.board import Board
from domain.model.game_state import GameState


class Game:
    def __init__(self, game_id=None, board=None, state=GameState.WAITING,
                 player_x_id=None, player_o_id=None, current_turn=None,
                 game_type="pvp", last_board=None):
        self.game_id = game_id or str(uuid.uuid4())
        self.board = board or Board()
        self.state = state
        self.player_x_id = player_x_id
        self.player_o_id = player_o_id
        self.current_turn = current_turn
        self.game_type = game_type
        self.last_board = last_board
    
    def to_dict(self):
        return {
            'game_id': self.game_id,
            'board': self.board.to_list(),
            'state': self.state.value,
            'player_x_id': self.player_x_id,
            'player_o_id': self.player_o_id,
            'current_turn': self.current_turn,
            'game_type': self.game_type,
            'last_board': self.last_board.to_list() if self.last_board else None
        }