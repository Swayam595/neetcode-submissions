class Solution:
    def climbStairs(self, n: int) -> int:
        return self.__climbStairsRecursively(n)
    
    def __climbStairsRecursively(self, n):
        if n <= 2:
            return n

        climb_1_step = self.__climbStairsRecursively(n - 1)
        climb_2_step = self.__climbStairsRecursively(n - 2)

        return climb_1_step + climb_2_step
