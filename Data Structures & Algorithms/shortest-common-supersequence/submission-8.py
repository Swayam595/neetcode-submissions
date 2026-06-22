class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # return self.__recursive(str1, str2, 0, 0)
        # return self.__topDown(str1, str2)
        return self.__bottomUp(str1, str2)
    
    # TC -> O(2 ^ (N + M))
    # SC -> O(M + N)
    def __recursive(self, s1: str, s2: str, i: int, j: int) -> str:
        if i == len(s1):
            return s2[j:]
        
        if j == len(s2):
            return s1[i:]
        
        if s1[i] == s2[j]:
            return s1[i] + self.__recursive(s1, s2, i + 1, j + 1)
        
        option1 = s1[i] + self.__recursive(s1, s2, i + 1, j)
        option2 = s2[j] + self.__recursive(s1, s2, i, j + 1)

        return option1 if len(option1) < len(option2) else option2

    # TC -> O(N * M)
    # SC -> O(N * M)
    def __topDown(self, s1: str, s2: str) -> str:
        N = len(s1)
        M = len(s2)

        cache = [[None] * (M + 1) for _ in range(N + 1)]
        return self.__topDownHelper(s1, s2, 0, 0, cache)

    # TC -> O(N * M)
    # SC -> O(N + M)
    def __topDownHelper(self, s1: str, s2: str, i: int, j: int, cache: List[List[str]]) -> str: 
        if i == len(s1):
            return s2[j:]
        
        if j == len(s2):
            return s1[i:]

        if cache[i][j] is not None:
            return cache[i][j]
        
        if s1[i] == s2[j]:
            cache[i][j] = s1[i] + self.__topDownHelper(s1, s2, i + 1, j + 1, cache)
        else:
            option1 = s1[i] + self.__topDownHelper(s1, s2, i + 1, j, cache)
            option2 = s2[j] + self.__topDownHelper(s1, s2, i, j + 1, cache)

            cache[i][j] = option1 if len(option1) < len(option2) else option2
        
        return cache[i][j]
    
    def __bottomUp(self, s1: str, s2: str) -> str:
        N = len(s1)
        M = len(s2)

        dp = [[""] * (M + 1) for _ in range(N + 1)]

        for j in range(M):
            dp[N][j] = s2[j:]
        
        for i in range(N):
            dp[i][M] = s1[i:]

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = s1[i] + dp[i + 1][j + 1]
                else:
                    option1 = s1[i] + dp[i + 1][j]
                    option2 = s2[j] + dp[i][j + 1]

                    dp[i][j] = option1 if len(option1) < len(option2) else option2
        
        return dp[0][0]

