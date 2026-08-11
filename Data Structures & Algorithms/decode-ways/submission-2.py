class Solution:
    def numDecodings(self, s: str) -> int:
        # return self.__recursive(0, s)
        return self.__top_down(s)

    def __top_down(self, s: str) -> int:
        cache = [-1] * len(s)

        return self.__top_down_helper(0, s, cache)
    
    def __top_down_helper(self, i: int, s: str, cache: List[int]) -> int:
        if i >= len(s):
            return 1

        if s[i] == '0':
            return 0
        
        if cache[i] != -1:
            return cache[i]

        take = 0
        if i + 1 < len(s) and int(s[i: i + 2]) < 27:
            take = self.__top_down_helper(i + 2, s, cache)
        
        
        skip = self.__top_down_helper(i + 1, s, cache)
        
        cache[i] = take + skip

        return cache[i]

    # TC -> O(2 ^ N)
    # SC -> O(N)
    def __recursive(self, i: int, s: str) -> int:
        if i >= len(s):
            return 1

        if s[i] == '0':
            return 0

        take = 0
        if i + 1 < len(s) and int(s[i: i + 2]) < 27:
            take = self.__recursive(i + 2, s)
        
        
        skip = self.__recursive(i + 1, s)
        
        return take + skip