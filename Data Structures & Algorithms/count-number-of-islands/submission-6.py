class Solution:
    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows in the grid
    # M -> # of cols in the grid
    def numIslands(self, grid: List[List[str]]) -> int:
        self.__ROWS = len(grid)
        self.__COLS = len(grid[0])
        visited = set()
        count = 0

        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if self.__is_island(r, c, grid, visited):
                    count += 1
        
        return count

    def __is_island(self, r: int, c: int, grid: List[List[int]], visited: set) -> bool:
        if not self.__is_valid_post(r, c, grid, visited):
            return False
        
        visited.add((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r_offset, c_offset in directions:
            r_new = r + r_offset
            c_new = c + c_offset
            self.__is_island(r_new, c_new, grid, visited)
        
        return True
    
    def __is_valid_post(self, r: int, c: int, grid: List[List[int]], visited: set) -> bool:
        return (
            0 <= r < self.__ROWS
            and 0 <= c < self.__COLS
            and grid[r][c] == "1"
            and (r, c) not in visited
        )
