class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # return self.__solve_n_queens_backtrack(n)
        return self.__solve_n_queens_backtrack_hashset(n)

    # TC -> O(N!)
    # where N! is the number of recursive calls 
    # SC -> O(N + N ^ 2) ~ O(N ^ 2)
    # O(N) recursion depth one level per row
    # O(N ^2) Board storage
    def __solve_n_queens_backtrack_hashset(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]
        self.__solve_n_queens_backtrack_hashset_helper(0, n, set(), set(), set(), board, ans)
        return ans
    
    def __solve_n_queens_backtrack_hashset_helper(
        self, 
        r: int, 
        n: int, 
        col: set,
        pos_diag: set, 
        neg_diag: set,
        board: List[List[str]],
        ans: List[List[str]]
    ) -> None:
        if r == n:
            copy = ["".join(row) for row in board]
            ans.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            self.__solve_n_queens_backtrack_hashset_helper(r + 1, n, col, pos_diag, neg_diag, board, ans)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."
        return
    
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
