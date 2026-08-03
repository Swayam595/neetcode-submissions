class Solution:
    __DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.__N = len(heights)
        self.__M = len(heights[0])

        # return self.__pacific_atlantic_back_track(heights)
        return self.__dfs(heights)

    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def __dfs(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        pacific = [[False] * (self.__M) for _ in range(self.__N)]
        atlantic = [[False] * (self.__M) for _ in range(self.__N)]

        for r in range(self.__N):
            self.__dfs_helper(r, 0, heights, pacific)
            self.__dfs_helper(r, self.__M - 1, heights, atlantic)

        for c in range(self.__M):
            self.__dfs_helper(0, c, heights, pacific)
            self.__dfs_helper(self.__N - 1, c, heights, atlantic)

        for r in range(self.__N):
            for c in range(self.__M):
                if pacific[r][c] and atlantic[r][c]:
                    ans.append([r, c])
        
        return ans

    
    def __dfs_helper(self, x: int, y: int, heights: List[List[int]], ocean: List[List[bool]]) -> None:
        ocean[x][y] = True

        for x_offset, y_offset in self.__DIRECTIONS:
            x_new = x + x_offset
            y_new = y + y_offset

            if self.__can_flow(x, y, x_new, y_new, heights, ocean):
                self.__dfs_helper(x_new, y_new, heights, ocean)

        return 
    
    def __can_flow(self, r: int, c: int, r_new: int, c_new: int, 
                    heights: List[List[int]], ocean: List[List[bool]]) -> bool:
        return (0 <= r_new < self.__N 
                and 0 <= c_new < self.__M 
                and heights[r][c] <= heights[r_new][c_new]
                and not ocean[r_new][c_new])
        
    # TC -> O(N * M * 4 ^ (N * M))
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def __pacific_atlantic_back_track(self, heights: List[List[int]]) -> List[List[int]]:       
        ans = []

        for r in range(self.__N):
            for c in range(self.__M):
                self.__can_flow_pacific = False
                self.__can_flow_atlantic = False
                self.__back_track_helper(r, c, heights, float('inf'))

                if self.__can_flow_to_both_ocean():
                    ans.append([r, c])
        
        return ans
    
    def __back_track_helper(self, x: int, y: int, heights: List[List[int]], prev_height: int):
        if x < 0 or y < 0:
            self.__can_flow_pacific = True
            return

        if x >= self.__N or y >= self.__M:
            self.__can_flow_atlantic = True
            return
        
        if prev_height < heights[x][y]:
            return
        
        tmp = heights[x][y]
        heights[x][y] = float('inf')

        for x_offset, y_offset in self.__DIRECTIONS:
            x_new = x + x_offset
            y_new = y + y_offset

            self.__back_track_helper(x_new, y_new, heights, tmp)
            if self.__can_flow_to_both_ocean():
                break
        
        heights[x][y] = tmp


    def __can_flow_to_both_ocean(self) -> bool:
        return self.__can_flow_pacific and self.__can_flow_atlantic