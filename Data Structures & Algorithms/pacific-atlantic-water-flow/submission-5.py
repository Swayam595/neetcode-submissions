class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.__ROWS = len(heights)
        self.__COLS = len(heights[0])

        return self.__dfs(heights)

    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def __dfs(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        pacific = [[False] * self.__COLS for _ in range(self.__ROWS)]
        atlantic = [[False] * self.__COLS for _ in range(self.__ROWS)]

        for c in range(self.__COLS):
            self.__dfs_helper(0, c, heights, pacific)
            self.__dfs_helper(self.__ROWS - 1, c, heights, atlantic)
        
        for r in range(self.__ROWS):
            self.__dfs_helper(r, 0, heights, pacific)
            self.__dfs_helper(r, self.__COLS - 1, heights, atlantic)

        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if pacific[r][c] and atlantic[r][c]:
                    ans.append([r, c])
        return ans
        
    def __dfs_helper(self, r: int, c: int, heights: List[List[int]], ocean: List[List[bool]]) -> None:
        ocean[r][c] = True
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r_offset, c_offset in directions:
            r_new = r + r_offset
            c_new = c + c_offset

            if self.__can_flow(r, c, r_new, c_new, heights, ocean):
                self.__dfs_helper(r_new, c_new, heights, ocean)
    
    def __can_flow(self, r: int, c: int, r_new: int, c_new: int, 
                    heights: List[List[int]], ocean: List[List[bool]]) -> bool:
        return (
            0 <= r_new < self.__ROWS
            and 0 <= c_new < self.__COLS
            and heights[r][c] <= heights[r_new][c_new]
            and not ocean[r_new][c_new]
        )