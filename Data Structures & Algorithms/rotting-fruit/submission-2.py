class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.__ROWS = len(grid)
        self.__COLS = len(grid[0])

        self.__q = deque()
        self.__visited = set()
        
        self.__get_rotten_fruit_queue(grid)
        self.__get_fresh_fruit_count(grid)

        time_elapsed = 0
        neighbours = [
                        [0, 1],
                        [0, -1],
                        [1, 0],
                        [-1, 0]
                    ]

        while len(self.__q) > 0 and self.__frest_fruit_count > 0:
            q_len = len(self.__q)
            for _ in range(q_len):
                r, c = self.__q.popleft()

                for dr, dc in neighbours:
                    if self.__cannot_rot(r + dr, c + dc, grid):
                       continue
                    
                    self.__frest_fruit_count -= 1
                    self.__q.append((r + dr, c + dc))
                    self.__visited.add((r + dr, c + dc))
            time_elapsed += 1
        
        if self.__frest_fruit_count > 0:
            return -1
        else:
            return time_elapsed
    
    def __get_rotten_fruit_queue(self, grid):
        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if grid[r][c] == 2:
                    self.__q.append((r, c))
                    self.__visited.add((r, c))
    
    def __get_fresh_fruit_count(self, grid):
        self.__frest_fruit_count = 0
        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if grid[r][c] == 1:
                    self.__frest_fruit_count += 1

    def __cannot_rot(self, r, c, grid):
        return (min(r, c) < 0 or
                r == self.__ROWS or
                c == self.__COLS or 
                (r, c) in self.__visited or
                grid[r][c] != 1)