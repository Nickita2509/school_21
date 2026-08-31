class GameService:
    def get_next_move(self, game):
        raise NotImplementedError
    
    def validate_board(self, game, new_board_matrix):
        raise NotImplementedError
    
    def check_game_over(self, board):
        raise NotImplementedError