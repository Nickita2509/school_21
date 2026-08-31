import uuid
from domain.model.board import Board


class Game:
    
    def __init__(self, game_id=None, board=None, last_board=None):
        self.game_id = game_id or str(uuid.uuid4())
        self.board = board or Board()
        self.last_board = last_board
    
    def to_dict(self):
        return {
            'game_id': self.game_id,
            'board': self.board.to_list(),
            'last_board': self.last_board.to_list() if self.last_board else None
        }