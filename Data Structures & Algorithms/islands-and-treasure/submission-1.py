class Solution:
    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        INF = 2 ** 31 - 1
        N = len(grid)
        M = len(grid[0])

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while len(q) > 0:
            r, c, val = q.popleft()

            for r_offset, c_offset in directions:
                r_new = r + r_offset
                c_new = c + c_offset
            
                if not(0 <= r_new < N and 0 <= c_new < M) or grid[r_new][c_new] != INF:
                    continue
                
                grid[r_new][c_new] = val + 1
                q.append((r_new, c_new, grid[r_new][c_new]))
        