class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.__climbStairsRecursively(n)
        # return self.__climbStairsTopDown(n, [-1 for _ in range(n + 1)])
        # return self.__climbStairsBottomUp(n)
        return self.__climbStairsBottomUpOptimized(n)
    
    def __climbStairsRecursively(self, n: int) -> int:
        if n <= 2:
            return n
        
        return self.__climbStairsRecursively(n - 1) + self.__climbStairsRecursively(n - 2)
    
    def __climbStairsTopDown(self, n: int, cache: List[int]) -> int:
        if n <= 2:
            return n
        
        if cache[n] != -1:
            return cache[n]
        
        cache[n] = self.__climbStairsTopDown(n - 1, cache) + self.__climbStairsTopDown(n - 2, cache)

        return cache[n]
    
    def __climbStairsBottomUp(self, n: int) -> int:
        if n <= 2:
            return n

        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 2

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[n]
    
    def __climbStairsBottomUpOptimized(self, n: int) -> int:
        if n <= 2:
            return n
        
        f_1 = 1
        f_2 = 2

        for i in range(3, n + 1):
            f_n = f_1 + f_2
            f_1 = f_2
            f_2 = f_n
        
        return f_n