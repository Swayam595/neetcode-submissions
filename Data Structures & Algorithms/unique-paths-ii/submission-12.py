class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # return self.__uniquePathsWithObstaclesRecursively(r = 0, c = 0, 
        #                                                   ROWS = len(obstacleGrid), 
        #                                                   COLS = len(obstacleGrid[0]),
        #                                                   grid = obstacleGrid) # Time Limit Exceeded
    
        # return self.__uniquePathsWithObstaclesTopDown(r = 0, c = 0, 
        #                                              ROWS = len(obstacleGrid), 
        #                                              COLS = len(obstacleGrid[0]), 
        #                                              grid = obstacleGrid,
        #                                              cache = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))])  # Time Limit Exceeded
        
        # return self.__uniquePathsWithObstaclesBottomUp(grid = obstacleGrid) # Accepted
        return self.__uniquePathsWithObstaclesBottomUpOptimized(grid = obstacleGrid) # Accepted

    # TC - O(2^(ROWS + COLS)) SC - O(2^(ROWS + COLS))
    def __uniquePathsWithObstaclesRecursively(self, 
                                              r: int, c: int, 
                                              ROWS: int, COLS: int,
                                              grid: List[List[int]]) -> int:
        if r == ROWS or c == COLS:
            return 0
        
        if grid[r][c] == 1:
            return 0
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        go_down = self.__uniquePathsWithObstaclesRecursively(r + 1, c, ROWS, COLS, grid)
        go_right = self.__uniquePathsWithObstaclesRecursively(r, c + 1, ROWS, COLS, grid)
        
        return go_down + go_right

    # TC - O(ROWS * COLS) SC - O(ROWS * COLS)
    def __uniquePathsWithObstaclesTopDown(self, 
                                         r: int, c: int, 
                                         ROWS: int, COLS: int,
                                         grid: List[List[int]],
                                         cache: List[List[int]]) -> int:
        if r == ROWS or c == COLS:
            return 0
        
        if grid[r][c] == 1:
            return 0
        
        if cache[r][c] != 0:
            return cache[r][c]
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        go_down = self.__uniquePathsWithObstaclesRecursively(r + 1, c, ROWS, COLS, grid)
        go_right = self.__uniquePathsWithObstaclesRecursively(r, c + 1, ROWS, COLS, grid)
        
        cache[r][c] = go_down + go_right

        return cache[r][c]

    # TC - O(ROWS * COLS) SC - O(ROWS * COLS)
    def __uniquePathsWithObstaclesBottomUp(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if grid[r][c] == 1:
                    continue
                elif r == ROWS - 1 and c == COLS - 1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        
        return dp[0][0]
    
    def __uniquePathsWithObstaclesBottomUpOptimized(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        prev_row = [0] * (COLS + 1)

        for r in range(ROWS - 1, -1, -1):
            curr_row = [0] * (COLS + 1)
            for c in range(COLS - 1, -1, -1):
                if grid[r][c] == 1:
                    continue
                elif r == ROWS - 1 and c == COLS - 1:
                    curr_row[c] = 1
                else:
                    curr_row[c] = prev_row[c] + curr_row[c + 1]
            prev_row = curr_row
        
        return prev_row[0]