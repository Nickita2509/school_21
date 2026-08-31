class GameDTO:
    
    def __init__(self, game_id=None, board=None):
        self.game_id = game_id
        self.board = board
    
    @staticmethod
    def from_dict(data):
        return GameDTO(
            game_id=data.get('game_id'),
            board=data.get('board')
        )
    
    def to_dict(self):
        return {
            'game_id': self.game_id,
            'board': self.board
        }