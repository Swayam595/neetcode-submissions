class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        return self.__uniquePathsRecursively(0, 0, ROWS, COLS) # Accepted
        # return self.__uniquePathsTopDown(0, 0, m, n, [[0] * n ])

    # TC - O(2^(ROWS + COLS)) SC - O(2^(ROWS + COLS))
    def __uniquePathsRecursively(self, r: int, c: int, ROWS: int, COLS: int) -> int:
        if r == ROWS or c == COLS:
            return 0
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        go_down = self.__uniquePathsRecursively(r + 1, c, ROWS, COLS)
        go_right = self.__uniquePathsRecursively(r, c + 1, ROWS, COLS)

        return go_down + go_right