class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        neighbours = [
            [0, 1], 
            [0, -1], 
            [1, 0], 
            [-1, 0], 
            [1, 1], 
            [1, -1], 
            [-1, 1], 
            [-1, -1]
            ]

        q = deque()
        visited = set()

        q.append((0, 0))
        visited.add((0, 0))

        shortest_path = 0

        while len(q) > 0:
            shortest_path += 1
            level_length = len(q)

            for _ in range(level_length):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return shortest_path
                
                for dr, dc in neighbours:
                    if self.__vertex_cannot_be_visited(grid, r + dr, c + dc, ROWS, COLS, visited):
                        continue
                    
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
        
        return -1


    
    def __vertex_cannot_be_visited(self, grid, r, c, ROWS, COLS, visited):
        return (min(r, c) < 0 or
                r == ROWS or 
                c == COLS or 
                (r, c) in visited or
                grid[r][c] == 1)
                
