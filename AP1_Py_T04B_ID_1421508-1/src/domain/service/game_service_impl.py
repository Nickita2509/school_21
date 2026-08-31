from domain.model.board import Board
from domain.model.game import Game
from domain.model.game_state import GameState
from domain.service.game_service import GameService


class GameServiceImpl(GameService):
    def __init__(self, game_repository):
        self.game_repository = game_repository
    
    def create_game(self, user_id, game_type):
        game = Game(player_x_id=user_id, game_type=game_type)
        if game_type == "pvc":
            game.state = GameState.PLAYER_X_TURN
            game.current_turn = Board.X
        self.game_repository.save(game)
        return game
    
    def join_game(self, game_id, user_id):
        game = self.game_repository.get(game_id)
        if game is None:
            raise ValueError("Игра не найдена")
        if game.state != GameState.WAITING:
            raise ValueError("Игра уже началась")
        if game.player_x_id == user_id:
            raise ValueError("Вы уже в этой игре")
        if game.player_o_id is not None:
            raise ValueError("Вторая сторона уже занята")
        
        game.player_o_id = user_id
        game.state = GameState.PLAYER_X_TURN
        game.current_turn = Board.X
        self.game_repository.save(game)
        return game
    
    def make_move(self, game_id, user_id, new_board_matrix):
        game = self.game_repository.get(game_id)
        if game is None:
            raise ValueError("Игра не найдена")
        if game.state in (GameState.WIN_X, GameState.WIN_O, GameState.DRAW):
            raise ValueError("Игра уже завершена")
        
        game.last_board = game.board.copy()
        new_board = self.validate_board(game, new_board_matrix, user_id)
        game.board = new_board
        
        result = self.check_game_over(game.board)
        if result == Board.X:
            game.state = GameState.WIN_X
        elif result == Board.O:
            game.state = GameState.WIN_O
        elif result == 'draw':
            game.state = GameState.DRAW
        else:
            current_turn_int = int(game.current_turn) if game.current_turn is not None else Board.X
            
            game.current_turn = Board.O if current_turn_int == Board.X else Board.X
            game.state = GameState.PLAYER_X_TURN if game.current_turn == Board.X else GameState.PLAYER_O_TURN
            
            if game.game_type == "pvc" and game.current_turn == Board.O:
                game = self.get_next_move(game)
                result = self.check_game_over(game.board)
                if result == Board.X:
                    game.state = GameState.WIN_X
                elif result == Board.O:
                    game.state = GameState.WIN_O
                elif result == 'draw':
                    game.state = GameState.DRAW
                else:
                    game.current_turn = Board.X
                    game.state = GameState.PLAYER_X_TURN
        
        self.game_repository.save(game)
        return game
    
    def get_game(self, game_id):
        return self.game_repository.get(game_id)
    
    def get_available_games(self):
        return self.game_repository.get_all_waiting()
    
    def _evaluate(self, board):
        winner = self._check_winner(board)
        if winner == Board.X:
            return 10
        elif winner == Board.O:
            return -10
        return 0
    
    def _check_winner(self, board):
        for i in range(3):
            if board.matrix[i][0] == board.matrix[i][1] == board.matrix[i][2] != Board.EMPTY:
                return board.matrix[i][0]
            if board.matrix[0][i] == board.matrix[1][i] == board.matrix[2][i] != Board.EMPTY:
                return board.matrix[0][i]
        if board.matrix[0][0] == board.matrix[1][1] == board.matrix[2][2] != Board.EMPTY:
            return board.matrix[0][0]
        if board.matrix[0][2] == board.matrix[1][1] == board.matrix[2][0] != Board.EMPTY:
            return board.matrix[0][2]
        return None
    
    def _minimax(self, board, depth, is_maximizing):
        score = self._evaluate(board)
        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        if not board.get_empty_cells():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for row, col in board.get_empty_cells():
                board.set_cell(row, col, Board.X)
                score = self._minimax(board, depth + 1, False)
                board.set_cell(row, col, Board.EMPTY)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for row, col in board.get_empty_cells():
                board.set_cell(row, col, Board.O)
                score = self._minimax(board, depth + 1, True)
                board.set_cell(row, col, Board.EMPTY)
                best_score = min(best_score, score)
            return best_score
    
    def _find_best_move(self, board):
        best_score = float('inf')
        best_move = None
        for row, col in board.get_empty_cells():
            board.set_cell(row, col, Board.O)
            score = self._minimax(board, 0, True)
            board.set_cell(row, col, Board.EMPTY)
            if score < best_score:
                best_score = score
                best_move = (row, col)
        return best_move
    
    def get_next_move(self, game):
        board = game.board.copy()
        move = self._find_best_move(board)
        if move:
            row, col = move
            board.set_cell(row, col, Board.O)
            game.board = board
        return game
    
    def validate_board(self, game, new_board_matrix, user_id):
        old_board = game.last_board if game.last_board else Board()
        new_board = Board(new_board_matrix)
        
        expected_symbol = int(game.current_turn) if game.current_turn is not None else None

        if game.player_x_id == user_id:
            user_symbol = Board.X
        elif game.player_o_id == user_id:
            user_symbol = Board.O
        else:
            raise ValueError("Вы не участвуете в этой игре")
        
        if user_symbol != expected_symbol:
            raise ValueError("Сейчас не ваш ход")
        
        changes = 0
        for i in range(3):
            for j in range(3):
                if old_board.matrix[i][j] != new_board.matrix[i][j]:
                    changes += 1
                    if old_board.matrix[i][j] != Board.EMPTY:
                        raise ValueError(f"Клетка [{i}][{j}] уже занята")
                    if new_board.matrix[i][j] != user_symbol:
                        raise ValueError(f"Можно ставить только свой символ")
        
        if changes != 1:
            raise ValueError(f"Нужно сделать ровно 1 ход, сделано {changes}")
        
        return new_board
    
    def check_game_over(self, board):
        winner = self._check_winner(board)
        if winner:
            return winner
        if not board.get_empty_cells():
            return 'draw'
        return None