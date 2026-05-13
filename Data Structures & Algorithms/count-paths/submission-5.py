class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        # return self.__uniquePathsRecursively(0, 0, ROWS, COLS) # Accepted
        # return self.__uniquePathsTopDown(0, 0, ROWS, COLS, [[0] * COLS for _ in range(ROWS)]) # Accepted
        # return self.__bottomUp(ROWS, COLS) # Accepted
        return self.__bottomUpOptimized(ROWS, COLS)

    # TC - O(2^(ROWS + COLS)) SC - O(2^(ROWS + COLS))
    def __uniquePathsRecursively(self, r: int, c: int, ROWS: int, COLS: int) -> int:
        if r == ROWS or c == COLS:
            return 0
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        go_down = self.__uniquePathsRecursively(r + 1, c, ROWS, COLS)
        go_right = self.__uniquePathsRecursively(r, c + 1, ROWS, COLS)

        return go_down + go_right

    # TC - O(ROWS * COLS) SC - O(ROWS * COLS)
    def __uniquePathsTopDown(self, r: int, c: int, ROWS: int, COLS: int, cache: List[List[int]]) -> int:
        if r == ROWS or c == COLS:
            return 0
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        if cache[r][c] > 0:
            return cache[r][c]
        
        go_down = self.__uniquePathsTopDown(r + 1, c, ROWS, COLS, cache)
        go_right = self.__uniquePathsTopDown(r, c + 1, ROWS, COLS, cache)

        cache[r][c] = go_down + go_right
    
        return cache[r][c]
    
    # TC - O(ROWS * COLS) SC - O(ROWS * COLS)
    def __bottomUp(self, ROWS: int, COLS: int) -> int:
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if r == ROWS - 1 and c == COLS - 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        
        return dp[0][0]
    
    # TC - O(ROWS * COLS) SC - O(COLS)
    def __bottomUpOptimized(self, ROWS: int, COLS: int) -> int:
        prev_row = [0] * (COLS + 1)
        
        for r in range(ROWS - 1, -1, -1):
            curr_row = [0] * (COLS + 1)
            for c in range(COLS - 1, -1, -1):
                if c == COLS - 1:
                    curr_row[c] = 1
                else:
                    curr_row[c] = curr_row[c + 1] + prev_row[c]

            prev_row = curr_row

        return prev_row[0]