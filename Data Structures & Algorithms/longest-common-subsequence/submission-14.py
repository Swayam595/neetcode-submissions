class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.__N = len(text1)
        self.__M = len(text2)

        # return self.__recursive(0, 0, text1, text2)
        # return self.__top_down(text1, text2)
        # return self.__bottom_up(text1, text2)
        return self.__bottom_up_optimized(text1, text2)

    # TC -> O(N * M)
    # SC -> O(M)
    # N -> len of text1
    # M -> len of text2
    def __bottom_up_optimized(self, t1: str, t2: str) -> int:
        dp = [0] * (self.__M + 1)

        for i in range(self.__N - 1, -1, -1):
            new_dp = [0] * (self.__M + 1)
            for j in range(self.__M - 1, -1, -1):
                if t1[i] == t2[j]:
                    new_dp[j] = 1 + dp[j + 1]
                else:
                    take_char_at_i_skip_char_at_j = new_dp[j + 1]
                    skip_char_at_i_take_char_at_j = dp[j]

                    new_dp[j] = max(take_char_at_i_skip_char_at_j, skip_char_at_i_take_char_at_j)

            dp = new_dp
        
        return dp[0]

    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> len of text1
    # M -> len of text2
    def __bottom_up(self, t1: str, t2: str) -> int:
        dp = [[0] * (self.__M + 1) for _ in range(self.__N + 1)]

        for i in range(self.__N - 1, -1, -1):
            for j in range(self.__M - 1, -1, -1):
                if t1[i] == t2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    take_char_at_i_skip_char_at_j = dp[i][j + 1]
                    skip_char_at_i_take_char_at_j = dp[i + 1][j]

                    dp[i][j] = max(take_char_at_i_skip_char_at_j, skip_char_at_i_take_char_at_j)

        return dp[0][0]

    # TC -> O(N * M)
    # SC -> O(N * M)
    # N -> len of text1
    # M -> len of text2
    def __top_down(self, t1: str, t2: str) -> int:
        cache = [[-1] * (self.__M) for _ in range(self.__N)]

        return self.__top_down_helper(0, 0, t1, t2, cache)

    def __top_down_helper(self, i: int, j: int, t1: str, t2: str, cache: List[List[int]]) -> int:
        if i >= self.__N or j >= self.__M:
            return 0
        
        if cache[i][j] != -1:
            return cache[i][j]

        if t1[i] == t2[j]:
            cache[i][j] = 1 + self.__top_down_helper(i + 1, j + 1, t1, t2, cache)
            return cache[i][j]
        
        take_char_at_i_skip_char_at_j = self.__top_down_helper(i, j + 1, t1, t2, cache)
        skip_char_at_i_take_char_at_j = self.__top_down_helper(i + 1, j, t1, t2, cache)

        cache[i][j] = max(take_char_at_i_skip_char_at_j, skip_char_at_i_take_char_at_j)

        return cache[i][j]
    
    # TC -> O(2 ^(N * M))
    # SC -> O(N * M)
    # N -> len of text1
    # M -> len of text2
    def __recursive(self, i: int, j: int, t1: str, t2: str) -> int:
        if i >= self.__N or j >= self.__M:
            return 0
        
        if t1[i] == t2[j]:
            return 1 + self.__recursive(i + 1, j + 1, t1, t2)
        
        take_char_at_i_skip_char_at_j = self.__recursive(i, j + 1, t1, t2)
        skip_char_at_i_take_char_at_j = self.__recursive(i + 1, j, t1, t2)

        return max(take_char_at_i_skip_char_at_j, skip_char_at_i_take_char_at_j)