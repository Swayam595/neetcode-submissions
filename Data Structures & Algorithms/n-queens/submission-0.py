class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.__solve_n_queens_backtrack(n)
    
    # TC -> O(N * N!)
    # where N! is the number of recursive calls 
    # O(N) per is_safe check
    # SC -> O(N + N ^ 2)
    # O(N) recursion depth one level per row
    # O(N ^2) Board storage
    def __solve_n_queens_backtrack(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        self.__solve_n_queens_backtrack_helper(0, n, res, board)
        return res
    
    def __solve_n_queens_backtrack_helper(self, r: int, n: int, res: List[List[srt]], board: List[List[str]]):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if self.__is_safe(r, c, board):
                board[r][c] = "Q"
                self.__solve_n_queens_backtrack_helper(r + 1, n, res, board)
                board[r][c] = "."
        return
    
    def __is_safe(self, r: int, c: int, board: List[List[str]]) -> bool:
        row = r - 1
        while row >= 0:
            if board[row][c] == 'Q':
                return False
            row -= 1
        
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == 'Q':
                return False
            row -= 1
            col += 1
        return True
