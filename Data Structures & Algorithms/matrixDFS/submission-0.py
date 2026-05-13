class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.__dfs(grid, 0, 0, set())

    def __dfs(self, grid, r, c, visited):
        ROWS_LEN = len(grid)
        COLS_LEN = len(grid[0])

        if (min(r, c) < 0 or
            r == ROWS_LEN or
            c == COLS_LEN or
            (r, c) in visited or
            grid[r][c] == 1):
            return 0
        
        if r == ROWS_LEN - 1 and c == COLS_LEN - 1:
            return 1


        visited.add((r, c))
        count = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r_offset, c_offset in directions:
            r_new = r + r_offset
            c_new = c + c_offset
            count += self.__dfs(grid, r_new, c_new, visited)

        visited.remove((r, c))
        return count 