class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()

        min_heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while len(min_heap) > 0:
            t, x, y = heapq.heappop(min_heap)

            if x == n - 1 and y == m - 1:
                return t

            for x_offset, y_offset in directions:
                x_new = x + x_offset
                y_new = y + y_offset

                if 0 <= x_new < n and 0 <= y_new < m and (x_new, y_new) not in visited:
                    visited.add((x_new, y_new))
                    time_to_next_grid = max(t, grid[x_new][y_new])
                    heapq.heappush(min_heap, (time_to_next_grid, x_new, y_new))
