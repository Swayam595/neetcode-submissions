from collections.abc import Callable

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.__ROWS = len(board)
        self.__COLS = len(board[0])
        self.__DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # return self.__dfs(board)
        return self.__bfs(board)
    
    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def __bfs(self, board: List[List[str]]) -> None:
        self.__traverse_from_boundary(self.__bfs_helper, board)
        self.__fill_board(board)

        return
        
    def __bfs_helper(self, r: int, c: int, board: List[List[str]]) -> None:
        q = deque()
        q.append((r, c))

        while len(q) > 0:
            r, c = q.popleft()

            if not self.__is_valid_pos(r, c, board):
                continue

            board[r][c] = "T"

            for r_offset, c_offset in self.__DIRECTIONS:
                r_new = r + r_offset
                c_new = c + c_offset
                q.append((r_new, c_new))
        return
    
    def __dfs(self, board: List[List[str]]) -> None:
        self.__traverse_from_boundary(self.__dfs_helper, board)
        
        self.__fill_board(board)

    def __dfs_helper(self, r: int, c: int, board: List[List[str]]) -> None:
        if not self.__is_valid_pos(r, c, board) or board[r][c] != "O":
            return
        
        board[r][c] = "T"
        
        for r_offset, c_offset in self.__DIRECTIONS:
            r_new = r + r_offset
            c_new = c + c_offset
            self.__dfs_helper(r_new, c_new, board)

    def __traverse_from_boundary(self, helper: Callable, board: List[List[str]]) -> None:
        for r in range(self.__ROWS):
            if board[r][0] == "O":
                helper(r, 0, board)
            if board[r][self.__COLS - 1] == "O":
                helper(r, self.__COLS - 1, board)
        
        for c in range(self.__COLS):
            if board[0][c] == "O":
                helper(0, c, board)
            if board[self.__ROWS - 1][c] == "O":
                helper(self.__ROWS - 1, c, board)
        
        return

    def __fill_board(self, board: List[List[str]]) -> None:
        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        return

    def __is_valid_pos(self, r: int, c: int, board: List[List[str]]) -> bool:
        return (
            0 <= r < self.__ROWS and
            0 <= c < self.__COLS and
            board[r][c] == "O"
        )