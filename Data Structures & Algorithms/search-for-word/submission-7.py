class Solution:
    # TC -> O(R * C * (4 ^ N))
    # SC -> O(N)
    # R -> # of rows
    # C -> # of cols
    # N -> len of word
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.__ROWS = len(board)
        self.__COLS = len(board[0])

        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if self.__search(0, r, c, word, board):
                    return True
        
        return False
    
    def __search(self, i: int, r: int, c: int, word: str, board: List[List[str]]) -> bool:
        if i >= len(word):
            return True

        if not self.__is_valid_index(r, c) or board[r][c] == "#":
            return False

        if board[r][c] != word[i]:
            return False
        
        char = board[r][c]
        board[r][c] = "#"
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        res = False
        for r_offset, c_offset in directions:
            r_new = r + r_offset 
            c_new = c + c_offset 
            if self.__search(i + 1, r_new, c_new, word, board):
                res = True
                break
        
        board[r][c] = char
        return res
    
    def __is_valid_index(self, r: int, c: int) -> bool:
        return 0 <= r < self.__ROWS and 0 <= c < self.__COLS