class Solution:
    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows in the grid
    # M -> # of cols in the grid
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.__ROWS = len(grid)
        self.__COLS = len(grid[0])
        max_area = 0
        seen = set()

        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                max_area = max(max_area, self.__explore(r, c, grid, seen))

        return max_area
    
    def __explore(self, r: int, c: int, grid: List[List[int]], seen: set) -> int:
        if not self.__is_valid_pos(r, c, grid, seen):
            return 0
        
        seen.add((r, c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        area = 1

        for r_offset, c_offset in directions:
            r_new = r + r_offset
            c_new = c + c_offset
            area += self.__explore(r_new, c_new, grid, seen)
        
        return area
    
    def __is_valid_pos(self, r: int, c: int, grid: List[List[int]], seen: set) -> bool:
        return (
            0 <= r < self.__ROWS and
            0 <= c < self.__COLS and
            grid[r][c] == 1 and
            (r, c) not in seen
        )
