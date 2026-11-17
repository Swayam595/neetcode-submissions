class Solution:
    # TC -> O(N * M * log(N))
    # SC -> O(N * M)
    # N -> # of rows
    # M -> # of cols
    def swimInWater(self, grid: List[List[int]]) -> int:
        time_taken = 0
        N = len(grid)
        M = len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        min_heap = list()
        visited = set()

        heapq.heappush(min_heap, (grid[0][0], (0 ,0)))
        visited.add((0, 0))

        while len(min_heap) > 0:
            t, (r, c) = heapq.heappop(min_heap)

            if r == N - 1 and c == M - 1:
                return t

            for r_offset, c_offset in directions:
                r_new = r + r_offset
                c_new = c + c_offset

                if not (0 <= r_new < N and 0 <= c_new < M) or (r_new, c_new) in visited:
                    continue

                time_to_next_gird = max(t, grid[r_new][c_new])
                heapq.heappush(min_heap, (time_to_next_gird, (r_new, c_new)))
                visited.add((r_new, c_new))