class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.__recursive(0, 0, m, n)
        return self.__top_down(m, n)

    def __top_down(self, M: int, N: int) -> int:
        cache = [[-1] * (N + 1) for _ in range(M + 1)]

        return self.__top_down_helper(0, 0, M, N, cache)

    # TC -> O((M + N) ^ 2)
    # SC -> O(M * N)
    def __top_down_helper(self, i: int, j: int, M: int, N: int, cache: List[List[int]]) -> int:
        if i == M - 1 and j == N - 1:
            return 1
        
        if i >= M or j >= N:
            return 0
        
        if cache[i][j] != -1:
            return cache[i][j]
        
        go_right = self.__top_down_helper(i, j + 1, M, N, cache)
        go_down = self.__top_down_helper(i + 1, j, M, N, cache)

        cache[i][j] = go_right + go_down

        return cache[i][j]

    # TC -> O(2 ^ (M + N))
    # SC -> O(M + N)
    def __recursive(self, i: int, j: int, m: int, n: int) -> int:
        if i == m - 1 and j == n - 1:
            return 1
        
        if i >= m or j >= n:
            return 0
        
        go_right = self.__recursive(i, j + 1, m, n)
        go_down = self.__recursive(i + 1, j, m, n)

        return go_right + go_down