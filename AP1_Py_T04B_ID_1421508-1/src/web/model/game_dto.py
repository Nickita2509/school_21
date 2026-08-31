class GameDTO:
    def __init__(self, game_id=None, board=None, state=None, player_x_id=None,
                 player_o_id=None, current_turn=None, game_type=None):
        self.game_id = game_id
        self.board = board
        self.state = state
        self.player_x_id = player_x_id
        self.player_o_id = player_o_id
        self.current_turn = current_turn
        self.game_type = game_type
    
    @staticmethod
    def from_dict(data):
        return GameDTO(
            game_id=data.get('game_id'),
            board=data.get('board'),
            state=data.get('state'),
            player_x_id=data.get('player_x_id'),
            player_o_id=data.get('player_o_id'),
            current_turn=data.get('current_turn'),
            game_type=data.get('game_type')
        )
    
    def to_dict(self):
        return {
            'game_id': self.game_id,
            'board': self.board,
            'state': self.state,
            'player_x_id': self.player_x_id,
            'player_o_id': self.player_o_id,
            'current_turn': self.current_turn,
            'game_type': self.game_type
        }