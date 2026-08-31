from domain.model.board import Board
from domain.model.game import Game
from domain.service.game_service import GameService


class GameServiceImpl(GameService):
    
    def __init__(self, repository):
        self.repository = repository

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
        
        self.repository.save(game)
        return game
    
    def validate_board(self, game, new_board_matrix):
        old_board = game.last_board if game.last_board else Board()
        new_board = Board(new_board_matrix)
        
        changes = 0
        for i in range(3):
            for j in range(3):
                if old_board.matrix[i][j] != new_board.matrix[i][j]:
                    changes += 1
                    if old_board.matrix[i][j] != Board.EMPTY:
                        raise ValueError(f"Клетка [{i}][{j}] уже занята")
                    if new_board.matrix[i][j] != Board.X:
                        raise ValueError(f"Можно ставить только X (1), получено {new_board.matrix[i][j]}")
        
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