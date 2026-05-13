class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        self.__visited = set()
        self.__ROWS_LEN = len(grid)
        self.__COLS_LEN = len(grid[0])

        for r in range(self.__ROWS_LEN):
            for c in range(self.__COLS_LEN):
                if grid[r][c] == "1" and (r, c) not in self.__visited:
                    self.__dfs(grid, r, c)
                    count += 1

        return count
    

    def __dfs(self, grid, r, c):
        if (min(r, c) < 0 or 
            r == self.__ROWS_LEN or
            c == self.__COLS_LEN or
            (r, c) in self.__visited or
            grid[r][c] == '0'):
            return 0

        self.__visited.add((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r_offset, c_offset in directions:
            r_new = r + r_offset
            c_new = c + c_offset

            self.__dfs(grid, r_new, c_new)
        
        return
