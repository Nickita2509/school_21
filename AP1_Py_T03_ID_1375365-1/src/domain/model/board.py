class Board:
    
    EMPTY = 0
    X = 1
    O = 2
    
    def __init__(self, matrix=None):
        if matrix is None:
            self.matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        else:
            self.matrix = [row[:] for row in matrix]
    
    def get_cell(self, row, col):
        return self.matrix[row][col]
    
    def set_cell(self, row, col, value):
        self.matrix[row][col] = value
    
    def is_empty(self, row, col):
        return self.matrix[row][col] == self.EMPTY
    
    def get_empty_cells(self):
        cells = []
        for i in range(3):
            for j in range(3):
                if self.matrix[i][j] == self.EMPTY:
                    cells.append((i, j))
        return cells
    
    def copy(self):
        return Board(self.matrix)
    
    def to_list(self):
        return [row[:] for row in self.matrix]