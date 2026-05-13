from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()

        q.append((0, 0))
        visited.add((0, 0))

        min_edges = 0

        while len(q) > 0:
            level_length = len(q)

            for _ in range(level_length):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return min_edges
                
                neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in neighbours:
                    r_new = r + dr
                    c_new = c + dc

                    if (min(r_new, c_new) < 0 or
                        r_new == ROWS or
                        c_new == COLS or
                        (r_new, c_new) in visited or
                        grid[r_new][c_new] == 1):
                        continue
                    
                    q.append((r_new, c_new))
                    visited.add((r_new, c_new))
            
            min_edges += 1
    
        return -1