from collections.abc import Callable

class Sets:
    def __init__(self, n: int) -> None:
        self.__parents = dict()
        self.__rank = dict()

        for i in range(n + 1):
            self.__parents[i] = i
            self.__rank[i] = 1
    
    def find(self, x: int) -> int:
        p = self.__parents[x]
        while p != self.__parents[p]:
            self.__parents[p] = self.__parents[self.__parents[p]]
            p = self.__parents[p]
        return p

    def union(self, u: int, v: int) -> bool:
        p1 = self.__parents[u]
        p2 = self.__parents[v]

        if p1 == p2:
            return False
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__parents[p2] = p1
            self.__rank[p1] += self.__rank[p2]
        else:
            self.__parents[p1] = p2
            self.__rank[p2] += self.__rank[p1]
        return True
    
    def connected(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.__ROWS = len(board)
        self.__COLS = len(board[0])
        self.__DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # return self.__dfs(board)
        # return self.__bfs(board)
        return self.__solve_union_find(board)

    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def __solve_union_find(self, board: List[List[str]]) -> None:
        sets = Sets((self.__ROWS * self.__COLS) + 1)

        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if board[r][c] != "O":
                    continue
                if self.__is_pos_at_edge(r, c):
                    sets.union(self.__ROWS * self.__COLS, r * self.__COLS + c)
                else:
                    for r_offset, c_offset in self.__DIRECTIONS:
                        r_new = r + r_offset
                        c_new = c + c_offset
                        if board[r_new][c_new] == "O":
                            sets.union(r * self.__COLS + c, r_new * self.__COLS + c_new)
        
        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if not sets.connected(self.__ROWS * self.__COLS, r * self.__COLS + c):
                    board[r][c] = "X"

    
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
    
    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
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
    def __is_pos_at_edge(self, r: int, c: int) -> bool:
        return (
            r == 0 or
            r == self.__ROWS - 1 or
            c == 0 or
            c == self.__COLS - 1
        )