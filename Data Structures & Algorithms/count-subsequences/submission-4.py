class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        # return self.__recursive(s, t, 0, 0)
        # return self.__topDown(s, t)
        return self.__bottomUpOptmized(s, t)
    
    # TC - O(2 ^ M)
    # SC - O(M)
    def __recursive(self, s: str, t: str, i: int, j: int) -> int:
        if j == len(t):
            return 1
        
        if i == len(s):
            return 0
        
        take = 0 
        if s[i] == t[j]:
            take = self.__recursive(s, t, i + 1, j + 1)
        skip = self.__recursive(s, t, i + 1, j)

        return take + skip

    # TC - O(M * N)
    # SC - O(M * N)
    def __topDown(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)

        cache = [[-1] * (M + 1) for _ in range(N)]

        return self.__topDownHelper(s, t, 0, 0, cache)
    
    # TC - O(M * N)
    # SC - O(M)
    def __topDownHelper(self, s: str, t: str, i: int, j: int, cache: List[List[int]]) -> int:
        if j == len(t):
            return 1

        if i == len(s):
            return 0
        
        if cache[i][j] != -1:
            return cache[i][j]
        
        take = 0 
        if s[i] == t[j]:
            take = self.__topDownHelper(s, t, i + 1, j + 1, cache)        
        skip = self.__topDownHelper(s, t, i + 1, j, cache)

        cache[i][j] = take + skip
        return cache[i][j]

    # TC - O(M * N)
    # SC - O(M * N)
    def __bottomUp(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)

        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for r in range(N + 1):
            dp[r][M] = 1
        
        for i in range(N - 1, - 1, -1):
            for j in range(M - 1, -1, -1):
                take = 0
                if s[i] == t[j]:
                    take = dp[i + 1][j + 1]
                skip = dp[i + 1][j]
                dp[i][j] = take + skip
        
        return dp[0][0]

    # TC - O(M * N)
    # SC - O(M)
    def __bottomUpOptmized(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)

        dp = [0] * (M + 1)
        dp[M] = 1

        for i in range(N - 1, -1, -1):
            new_dp = [0] * (M + 1)
            new_dp[M] = 1
            for j in range(M - 1, -1, -1):
                take = 0
                if s[i] == t[j]:
                    take = dp[j + 1]
                skip = dp[j]
                new_dp[j] = take + skip
            dp = new_dp
        
        return dp[0]