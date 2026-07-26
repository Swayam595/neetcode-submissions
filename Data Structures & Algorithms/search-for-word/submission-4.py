class Solution:
    __DIRECTIONS_OFFSET = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # TC -> O(N * M)
    # SC -> O(N * M)
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.__N = len(board)
        self.__M = len(board[0])

        for i in range(self.__N):
            for j in range(self.__M):
                seen = set()
                if self.__search(i, j, 0, board, word, seen):
                    return True
        
        return False
    
    def __search(self, x: int, y: int, i: int, board: List[List[str]], word: str, seen: set) -> bool:
        if i >= len(word):
            return True

        if x < 0 or x >= self.__N or y < 0 or y >= self.__M:
            return False

        if (x, y) in seen or board[x][y] != word[i]:
            return False

        seen.add((x, y))

        for x_offset, y_offset in self.__DIRECTIONS_OFFSET:
            x_new = x + x_offset
            y_new = y + y_offset
            
            if self.__search(x_new, y_new, i + 1, board, word, seen):
                return True
        
        seen.remove((x, y))
        return False