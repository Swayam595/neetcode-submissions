class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return self.__recursive(text1, text2, 0, 0)
        # return self.__topDown(text1, text2)
        return self.__bottomUp(text1, text2)
    
    # TC - O(2 ^ (N + M))
    # SC - O(N + M)
    def __recursive(self, s1: str, s2: str, i1: int, i2: int) -> int:
        if i1 == len(s1) or i2 == len(s2):
            return 0
        
        if s1[i1] == s2[i2]:
            return 1 + self.__recursive(s1, s2, i1 + 1, i2 + 1)
        else:
            take_i1 = self.__recursive(s1, s2, i1, i2 + 1)
            take_i2 = self.__recursive(s1, s2, i1 + 1, i2)

            return max(take_i1, take_i2)

    # TC - O(N * M)
    # SC - O(N * M)
    def __topDown(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        cache = [[-1] * (M) for _ in range(N)]

        return self.__topDownHelper(s1, s2, 0, 0, cache)
    
    # TC - O(N * M)
    # SC - O(N + M)
    def __topDownHelper(self, s1: str, s2: str, i1: int, i2: int, cache: List[List[int]]) -> int:
        if i1 == len(s1) or i2 == len(s2):
            return 0
        
        if cache[i1][i2] != -1:
            return cache[i1][i2]
        
        if s1[i1] == s2[i2]:
            cache[i1][i2] = 1 + self.__topDownHelper(s1, s2, i1 + 1, i2 + 1, cache)
        else:
            take_i1 = self.__topDownHelper(s1, s2, i1, i2 + 1, cache)
            take_i2 = self.__topDownHelper(s1, s2, i1 + 1, i2, cache)

            cache[i1][i2] = max(take_i1, take_i2)
        
        return cache[i1][i2]

    # TC -> O(N * M)
    # SC -> O(N * M)
    def __bottomUp(self, s1: str, s2: str) -> int:
        N = len(s1)
        M = len(s2)

        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i1 in range(N - 1, -1, -1):
            for i2 in range(M - 1, -1, -1):
                if s1[i1] == s2[i2]:
                    dp[i1][i2] = 1 + dp[i1 + 1][i2 + 1]
                else:
                    dp[i1][i2] = max(dp[i1 + 1][i2], dp[i1][i2 + 1])
        
        return dp[0][0]
