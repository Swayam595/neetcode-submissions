class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.__ROWS = len(heights)
        self.__COLS = len(heights[0])
        self.__DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # return self.__dfs(heights)
        return self.__bfs(heights)
    
    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def __bfs(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = self.__generate_ocean_array(2)
        pacific_queue = deque()
        atlantic_queue = deque()

        for c in range(self.__COLS):
            pacific_queue.append([0, c])
            atlantic_queue.append([self.__ROWS - 1, c])

        for r in range(self.__ROWS):
            pacific_queue.append([r, 0])
            atlantic_queue.append([r, self.__COLS - 1])

        self.__bfs_helper(pacific_queue, heights, pacific)
        self.__bfs_helper(atlantic_queue, heights, atlantic)

        return self.__generate_ans(pacific, atlantic)
    
    def __bfs_helper(self, q: deque, heights: List[List[int]], ocean: List[List[bool]]) -> None:
        while len(q) > 0:
            r, c = q.popleft()
            ocean[r][c] = True
            
            for r_offset, c_offset in self.__DIRECTIONS:
                r_new = r + r_offset
                c_new = c + c_offset

                if self.__can_flow(r, c, r_new, c_new, heights, ocean):
                    q.append([r_new, c_new])

        return

    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def __dfs(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = self.__generate_ocean_array(2)
        
        for c in range(self.__COLS):
            self.__dfs_helper(0, c, heights, pacific)
            self.__dfs_helper(self.__ROWS - 1, c, heights, atlantic)
        
        for r in range(self.__ROWS):
            self.__dfs_helper(r, 0, heights, pacific)
            self.__dfs_helper(r, self.__COLS - 1, heights, atlantic)

        
        return self.__generate_ans(pacific, atlantic)
        
    def __dfs_helper(self, r: int, c: int, heights: List[List[int]], ocean: List[List[bool]]) -> None:
        ocean[r][c] = True

        for r_offset, c_offset in self.__DIRECTIONS:
            r_new = r + r_offset
            c_new = c + c_offset

            if self.__can_flow(r, c, r_new, c_new, heights, ocean):
                self.__dfs_helper(r_new, c_new, heights, ocean)

    def __generate_ocean_array(self, count: int) -> List[List[List[bool]]]:
        return [
                    [
                        [False] * (self.__COLS) for _ in range(self.__ROWS)
                    ] for _ in range(count)
                ]
    
    def __can_flow(self, r: int, c: int, r_new: int, c_new: int, 
                    heights: List[List[int]], ocean: List[List[bool]]) -> bool:
        return (
            0 <= r_new < self.__ROWS
            and 0 <= c_new < self.__COLS
            and heights[r][c] <= heights[r_new][c_new]
            and not ocean[r_new][c_new]
        )
    
    def __generate_ans(self, pacific: List[List[bool]], atlantic: List[List[bool]]) -> List[List[int]]:
        ans = []
        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if pacific[r][c] and atlantic[r][c]:
                    ans.append([r, c])
        return ans