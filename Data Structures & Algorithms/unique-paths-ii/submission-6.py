class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        self.__findObstacles(obstacleGrid, ROWS, COLS)

        # return self.__uniquePathsWithObstaclesRecursively(0, 0, ROWS, COLS) # Time Limit Exceeded
        # return self.__uniquePathsWithObstaclesTopDown(0, 0, ROWS, COLS, [[0] * COLS for _ in range(ROWS)]) # Time Limit Exceeded
        # return self.__uniquePathsWithObstaclesBottomUp(ROWS, COLS) # Accepted
        return self.__uniquePathsWithObstaclesBottomUpOptimized(ROWS, COLS)

    # TC - O(ROWS * COLS) SC - O (ROWS * COLS)
    def __findObstacles(self, obstacleGrid: List[List[int]], ROWS: int, COLS: int) -> None:
        self.__obstacles_seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if obstacleGrid[r][c] == 1:
                    self.__obstacles_seen.add((r, c))
    
    # TC - O(2 ^ (ROWS + COLS)) SC - O(2 ^(ROWS + COLS))
    def __uniquePathsWithObstaclesRecursively(self, r, c, ROWS, COLS):
        if r == ROWS or c == COLS:
            return 0
        
        if (r, c) in self.__obstacles_seen:
            return 0
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        go_down = self.__uniquePathsWithObstaclesRecursively(r + 1, c, ROWS, COLS)
        go_right = self.__uniquePathsWithObstaclesRecursively(r, c + 1, ROWS, COLS)

        return go_down + go_right

    # TC - O(ROWS * COLS) SC - O(ROWS * COLS)
    def __uniquePathsWithObstaclesTopDown(self, r, c, ROWS, COLS, cache):
        if r == ROWS or c == COLS:
            return 0
        
        if (r, c) in self.__obstacles_seen:
            return 0
        
        if cache[r][c] != 0:
            return cache[r][c]
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        go_down = self.__uniquePathsWithObstaclesRecursively(r + 1, c, ROWS, COLS)
        go_right = self.__uniquePathsWithObstaclesRecursively(r, c + 1, ROWS, COLS)

        cache[r][c] = go_down + go_right

        return cache[r][c]
    
    # TC - O(ROWS * COLS) SC - O(ROWS * COLS)
    def __uniquePathsWithObstaclesBottomUp(self, ROWS, COLS):
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if (r, c) in self.__obstacles_seen:
                    continue
                elif r == ROWS - 1 and c == COLS - 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        
        return dp[0][0]

    # TC - O(ROWS * COLS) SC - O(max(COLS, len(self.__obstacles_seen)))
    def __uniquePathsWithObstaclesBottomUpOptimized(self, ROWS, COLS):
        prev_row = [0] * (COLS + 1)

        for r in range(ROWS - 1, -1, -1):
            curr_row = [0] * (COLS + 1)
            for c in range(COLS - 1, -1, -1):
                if (r, c) in self.__obstacles_seen:
                    continue
                elif c == COLS - 1 and r == ROWS - 1:
                    curr_row[c] = 1
                else:
                    curr_row[c] = curr_row[c + 1] + prev_row[c]
                    
            prev_row = curr_row
        
        return prev_row[0]
                    