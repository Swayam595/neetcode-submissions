class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.__recursive(s)
    
    def __recursive(self, s: str) -> int:
        N = len(s)
        cache = [[-1] * N for _ in range(N)]

        for i in range(N):
            self.__recursiveHelper(i, i, s, cache)
            self.__recursiveHelper(i, i + 1, s, cache)
        
        return max(max(row) for row in cache if row != -1)
    
    def __recursiveHelper(self, i: int, j: int, s: str, cache: List[List[int]]) -> int:
        if i < 0 or j == len(s):
            return 0
        
        if cache[i][j] != -1:
            return cache[i][j]

        if s[i] == s[j]:
            length = 1 if i == j else 2
            cache[i][j] = length + self.__recursiveHelper(i - 1, j + 1, s, cache)
        else:
            take_char_at_i = self.__recursiveHelper(i, j + 1, s, cache)
            take_char_at_j = self.__recursiveHelper(i - 1, j, s, cache)
            cache[i][j] = max(take_char_at_i, take_char_at_j)
        
        return cache[i][j]