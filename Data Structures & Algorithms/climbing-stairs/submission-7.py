class Solution:
    def climbStairs(self, n: int) -> int:
        return self.__climbStairsRecursively(n)
    
    def __climbStairsRecursively(self, n: int) -> int:
        if n <= 2:
            return n
        
        return self.__climbStairsRecursively(n - 1) + self.__climbStairsRecursively(n - 2)