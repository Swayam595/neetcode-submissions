class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.__climbStairsRecursively(n)
        return self.__climbStairsTopDown(n, [-1 for _ in range(n + 1)])
    
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