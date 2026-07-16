from grid_position import GridPosition

class Grid:
    def __init__(self, rows: int, cols: int) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__grid = None

        self.initGrid()

    def initGrid(self) -> None:
        self.__grid = [[GridPosition.EMPTY] * self.__cols for _ in range(self.__rows)]

    def get_grid(self) -> list[list[GridPosition]]:
        return self.__grid

    def get_column_count(self) -> int:
        return self.__cols
    
    def place_disk(self, col_pos: int, piece: GridPosition) -> int:
        if col_pos < 0 or col_pos >= self.__cols:
            raise ValueError("Invalid Column")
        
        if piece == GridPosition.EMPTY:
            raise ValueError("Invalid piece")
        
        for row in range(self.__rows - 1, -1, -1):
            if self.__grid[row][col_pos] == GridPosition.EMPTY:
                self.__grid[row][col_pos] = piece
                return row
    
    def check_win(self, connect_n: int, row: int, col: int, piece: GridPosition) -> bool:
        return (self.__check_anti_diagonal(connect_n, row, col, piece) 
                or self.__check_diagonal(connect_n, row, col, piece)
                or self.__check_horizontal(connect_n, row, col, piece)
                or self.__check_vertical(connect_n, row, col, piece))                     

    def __check_vertical(self, connect_n: int, row: int, col: int, piece: GridPosition) -> bool:
        count = 0

        for r in range(self.__rows):
            if self.__grid[r][col] == piece:
                count += 1
            else:
                count = 0
            
            if count == connect_n:
                return True
        
        return False

    def __check_horizontal(self, connect_n: int, row: int, col: int, piece: GridPosition) -> bool:
        count = 0
        
        for c in range(self.__cols):
            if self.__grid[row][c] == piece:
                count += 1
            else:
                count = 0
            
            if count == connect_n:
                return True
        
        return False
    
    def __check_diagonal(self, connect_n: int, row: int, col: int, piece: GridPosition) -> bool:
        count = 0

        for r in range(self.__rows):
            c = row + col - r
            
            if 0 <= c < self.__cols and self.__grid[r][c] == piece:
                count += 1
            else:
                count = 0

            if count == connect_n:
                return True
        
        return False
    
    def __check_anti_diagonal(self, connect_n: int, row: int, col: int, piece: GridPosition) -> bool:
        count = 0

        for r in range(self.__rows):
            c = col - row + r

            if 0 <= c < self.__cols and self.__grid[r][c] == piece:
                count += 1
            else:
                count = 0
            
            if count == connect_n:
                return True
            c += 1
        
        return False