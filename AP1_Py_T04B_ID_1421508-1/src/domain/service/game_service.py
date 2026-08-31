class GameService:
    def create_game(self, user_id, game_type):
        raise NotImplementedError
    
    def join_game(self, game_id, user_id):
        raise NotImplementedError
    
    def make_move(self, game_id, user_id, new_board_matrix):
        raise NotImplementedError
    
    def get_game(self, game_id):
        raise NotImplementedError
    
    def get_available_games(self):
        raise NotImplementedError
    
    def get_next_move(self, game):
        raise NotImplementedError
    
    def validate_board(self, game, new_board_matrix, user_id):
        raise NotImplementedError
    
    def check_game_over(self, board):
        raise NotImplementedError