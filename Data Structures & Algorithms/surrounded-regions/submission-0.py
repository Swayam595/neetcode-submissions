class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.__ROWS = len(board)
        self.__COLS = len(board[0])

        return self.__dfs(board)
    
    def __dfs(self, board: List[List[str]]) -> None:
        for r in range(self.__ROWS):
            if board[r][0] == "O":
                self.__dfs_helper(r, 0, board)
            if board[r][self.__COLS - 1] == "O":
                self.__dfs_helper(r, self.__COLS - 1, board)
        
        for c in range(self.__COLS):
            if board[0][c] == "O":
                self.__dfs_helper(0, c, board)
            if board[self.__ROWS - 1][c] == "O":
                self.__dfs_helper(self.__ROWS - 1, c, board)
        
        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

    def __dfs_helper(self, r: int, c: int, board: List[List[str]]) -> None:
        if not self.__is_valid_pos(r, c, board) or board[r][c] != "O":
            return
        
        board[r][c] = "T"
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r_offset, c_offset in directions:
            r_new = r + r_offset
            c_new = c + c_offset
            self.__dfs_helper(r_new, c_new, board)

    def __is_valid_pos(self, r: int, c: int, board: List[List[str]]) -> bool:
        return (
            0 <= r < self.__ROWS and
            0 <= c < self.__COLS and
            board[r][c] == "O"
        )