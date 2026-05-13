class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.__ROWS = len(grid)
        self.__COLS = len(grid[0])

        self.__q = deque()
        self.__visited = set()

        self.__get_rotten_queue(grid)
        self.__get_fresh_fruits_count(grid)

        mins_elapsed = 0

        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        mins_elapsed = 0
        while len(self.__q) > 0:
            r, c, mins_elapsed = self.__q.popleft()

            for dr, dc in neighbours:
                if self.__cannot_rot(r + dr, c + dc, grid):
                    continue
                
                self.__fresh_fruits_count -= 1

                if self.__fresh_fruits_count == 0:
                    return mins_elapsed + 1
                
                self.__q.append((r + dr, c + dc, mins_elapsed + 1))
                self.__visited.add((r + dr, c + dc))
        
        if self.__fresh_fruits_count > 0:
            return -1
        else:
            return 0

    
    def __get_rotten_queue(self, grid):
        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if grid[r][c] == 2:
                    self.__q.append((r, c, 0))
    
    def __get_fresh_fruits_count(self, grid):
        self.__fresh_fruits_count = 0
        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                if grid[r][c] == 1:
                    self.__fresh_fruits_count += 1
    
    def __cannot_rot(self, r, c, grid):
        return (min(r, c) < 0 or
                r == self.__ROWS or
                c == self.__COLS or 
                (r, c) in self.__visited or
                grid[r][c] != 1)
