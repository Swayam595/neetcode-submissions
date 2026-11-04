class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        q = deque()
        fresh_fruit = 0
        seen = set()

        for r in range(N):
            for c in range(M):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        
        while len(q) > 0 and fresh_fruit > 0:
            time += 1
            total_rotten_fruits = len(q)

            for _ in range(total_rotten_fruits):
                r, c = q.popleft()
                for r_offset, c_offset in directions:
                    r_new = r + r_offset
                    c_new = c + c_offset

                    if 0 <= r_new < N and 0 <= c_new < M and grid[r_new][c_new] == 1 and (r_new, c_new) not in seen:
                        q.append((r_new, c_new))
                        fresh_fruit -= 1
                        seen.add((r_new, c_new))
                    
                
        
        return time if fresh_fruit == 0 else -1