class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # return self.__recursive(word1, word2, 0, 0, len(word1), len(word2))
        # return self.__topDown(word1, word2)
        return self.__bottomUp(word1, word2)
    
    # TC -> O(2 ^ (N + M))
    # SC -> O(N + M)
    def __recursive(self, s1: str, s2: str, i: int, j: int, N: int, M: int) -> int:
        if i == N:
            return M - j
        
        if j == M:
            return N - i
        
        if s1[i] == s2[j]:
            return self.__recursive(s1, s2, i + 1, j + 1, N, M)
        else:
            replace = self.__recursive(s1, s2, i + 1, j + 1, N, M)
            delete = self.__recursive(s1, s2, i + 1, j, N, M)
            insert = self.__recursive(s1, s2, i, j + 1, N, M)
            return min(replace, delete, insert) + 1

    # TC -> O(N * M)
    # SC -> O(N * M)
    def __topDown(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        memo = [[-1] * (M + 1) for _ in range(N)]

        return self.__topDownHelper(s1, s2, 0, 0, N, M, memo)

    # TC -> O(N * M)
    # SC -> O(N + M)
    def __topDownHelper(self, s1: str, s2: str, i: int, j: int, 
                        N: int, M: int, memo: List[List[int]]) -> int: 
        if i == N:
            return M - j

        if j == M:
            return N - i

        if memo[i][j] != -1:
            return memo[i][j]
        
        if s1[i] == s2[j]:
            memo[i][j] = self.__topDownHelper(s1, s2, i + 1, j + 1, N, M, memo)
        else:
            replace = self.__topDownHelper(s1, s2, i + 1, j + 1, N, M, memo)
            delete = self.__topDownHelper(s1, s2, i + 1, j, N, M, memo)
            insert = self.__topDownHelper(s1, s2, i, j + 1, N, M, memo)

            memo[i][j] = min(replace, delete, insert) + 1
        
        return memo[i][j]

    # TC -> O(N * M)
    # SC -> O(N * M)
    def __bottomUp(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        dp = [[0] * (M + 1) for i in range(N + 1)]
        
        for j in range(M - 1, -1, -1):
            dp[N][j] = M - j
        
        for i in range(N - 1, -1, -1):
            dp[i][M] = N - i

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    replace = dp[i + 1][j + 1]
                    delete  = dp[i + 1][j]
                    insert = dp[i][j + 1]

                    dp[i][j] = 1 + min(replace, delete, insert)

        return dp[0][0]
