class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.__ROWS_LEN = len(grid)
        self.__COLS_LEN = len(grid[0])

        self.__visited = set()
        max_area = 0

        for r in range(self.__ROWS_LEN):
            for c in range(self.__COLS_LEN):
                if grid[r][c] == 1 and (r, c) not in self.__visited:
                    curr_area = self.__dfs(grid, r, c)
                    max_area = max(max_area, curr_area)
            
        return max_area
    
    def __dfs(self, grid, r, c):
        if (min(r, c) < 0 or
            r == self.__ROWS_LEN or
            c == self.__COLS_LEN or
            (r, c) in self.__visited or
            grid[r][c] == 0):
            return 0
        
        self.__visited.add((r, c))
        area = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r_offset, c_offset in directions:
            r_new = r + r_offset
            c_new = c + c_offset
            area += self.__dfs(grid, r_new, c_new)

        return area