class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.__recursion(n)
        return self.__topDown(n)
        # return self.__bottomUp(n)
        # return self.__bottomUpOptimized(n)

    # TC - O(2 ^ N)
    # SC - O(N)
    def __recursion(self, n: int) -> int:
        if n <= 2:
            return n
        
        take_1_step = self.__recursion(n - 1)
        take_2_step = self.__recursion(n - 2)

        return take_1_step + take_2_step

    # TC - O(N ^ 2)
    # SC - O(N)
    def __topDown(self, n: int) -> int:
        cache = [-1] * (n + 1)
        return self.__topDownHelper(n, cache)

    def __topDownHelper(self, n: int, cache: list[int]) -> int:
        if n <= 2:
            return n
        
        if cache[n] != -1:
            return cache[n]
        
        take_1_step = self.__topDownHelper(n - 1, cache)
        take_2_step = self.__topDownHelper(n - 2, cache)

        cache[n] = take_1_step + take_2_step

        return cache[n]

    # TC - O(N)
    # SC -O(N)
    def __bottomUp(self, n: int) -> int:
        memo = [0] * (n + 1)

        for i in range(n + 1):
            if i <= 2:
                memo[i] = i
            else:
                take_1_step = memo[i - 1]
                take_2_step = memo[i - 2]

                memo[i] = take_1_step + take_2_step
                
        return memo[n]

    # TC - O(N)
    # SC - O(1)
    def __bottomUpOptimized(self, n: int) -> int:
        if n <= 2:
            return n

        take_1_step = 1
        take_2_step = 2
        for i in range(3, n + 1):
            if i > 2:
                temp = take_1_step + take_2_step
                take_1_step = take_2_step
                take_2_step = temp

        return take_2_step