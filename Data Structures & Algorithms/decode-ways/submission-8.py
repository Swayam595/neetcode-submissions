class Solution:
    def numDecodings(self, s: str) -> int:
        # return self.__recursive(0, s)
        # return self.__top_down(s)
        # return self.__bottom_up(s)
        return self.__bottom_up_optimized(s)

    # TC -> O(N)
    # SC -> O(1)
    def __bottom_up_optimized(self, s: str) -> int:
        n = len(s)
        
        dp_1 = 1
        dp_2 = 0
        dp_n = 0

        for i in range(n - 1, -1, -1):
            if s[i] != '0':
                take = 0
                if i + 1 < n and int(s[i:i+2]) < 27:
                    take = dp_2
                skip = dp_1

                dp_n = take + skip

            dp_2 = dp_1
            dp_1 = dp_n
            dp_n = 0

        return dp_1

    # TC -> O(N)
    # SC -> O(N)
    def __bottom_up(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            take = 0
            skip = 0
            
            if s[i] != '0':
                if i + 1 < n and int(s[i:i+2]) < 27:
                    take = dp[i + 2]
                    
                skip = dp[i + 1]

            dp[i] = take + skip
        
        return dp[0]

    # TC -> O(N)
    # SC -> O(N)
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