class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Time Limit Exceeded
        # return self.__longestCommonSubsequenceRecursively(i = 0, j = 0, 
        #                                                   t1 = text1, t2 = text2)

        # Time Limit Exceeded
        # return self.__longestCommonSubsequenceTopDown(0, 0, 
        #                                               text1, text2, 
        #                                               [[0] * len(text1) for _ in range(len(text2))])

        # Accepted
        # return self.__longestCommonSubsequenceBottomUp(text1, text2)

        # Accepted
        return self.__longestCommonSubsequenceBottomUpOptimized(text1, text2)

    # TC - O(2^(n + m) SC - O(n + m)
    # where n = len(t1)
    #       m = len(t2)
    def __longestCommonSubsequenceRecursively(self, i: int, j: int, 
                                              t1: str, t2: str) -> int:
        if i == len(t1) or j == len(t2):
            return 0
        
        if t1[i] == t2[j]:
            return 1 + self.__longestCommonSubsequenceRecursively(i + 1, j + 1, t1, t2)
        
        take_char_at_i_skip_char_at_j = self.__longestCommonSubsequenceRecursively(i, j + 1, t1, t2)
        take_char_at_j_skip_char_at_i = self.__longestCommonSubsequenceRecursively(i + 1, j, t1, t2)

        return max(take_char_at_i_skip_char_at_j, take_char_at_j_skip_char_at_i)

    # TC - O(n * m) SC - O(n * m)
    # where n = len(t1)
    #       m = len(t2)
    def __longestCommonSubsequenceTopDown(self, i: int, j: int, 
                                              t1: str, t2: str,
                                              cache: List[List[int]]) -> int:
        if i == len(t1) or j == len(t2):
            return 0

        if cache[i][j] != 0:
            return cache[i][j]

        if t1[i] == t2[j]:
            return 1 + self.__longestCommonSubsequenceTopDown(i + 1, j + 1, t1, t2, cache)

        
        take_char_at_i_skip_char_at_j = self.__longestCommonSubsequenceRecursively(i, j + 1, t1, t2)
        take_char_at_j_skip_char_at_i = self.__longestCommonSubsequenceRecursively(i + 1, j, t1, t2)

        cache[i][j] = max(take_char_at_i_skip_char_at_j, take_char_at_j_skip_char_at_i)
    
        return cache[i][j]
    
    # TC - O(n * m) SC - O(n * m)
    # where n = len(t1)
    #       m = len(t2)
    def __longestCommonSubsequenceBottomUp(self, t1: str, t2: str) -> int:
        n = len(t1)
        m = len(t2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, - 1, -1):
            for j in range(m - 1, -1, -1):
                if t1[i] == t2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]

    # TC - O(n * m) SC - O(m)
    # where n = len(t1)
    #       m = len(t2)
    def __longestCommonSubsequenceBottomUpOptimized(self, t1: str, t2: str) -> int:
        n = len(t1)
        m = len(t2)

        prev_row = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            curr_row = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                if t1[i] == t2[j]:
                    curr_row[j] = 1 + prev_row[j + 1]
                else:
                    curr_row[j] = max(prev_row[j], curr_row[j + 1])
            prev_row = curr_row
        
        return prev_row[0]