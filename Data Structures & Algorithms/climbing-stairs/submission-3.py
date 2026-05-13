class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.__climbStairsRecursively(n)

        if n <= 2:
            return n
        self.__cache = [-1] * (n + 1)
        self.__climbStairsBottomUp(n)
        return self.__cache[n]
    
    def __climbStairsRecursively(self, n):
        if n <= 2:
            return n

        climb_1_step = self.__climbStairsRecursively(n - 1)
        climb_2_step = self.__climbStairsRecursively(n - 2)

        return climb_1_step + climb_2_step

    def __climbStairsBottomUp(self, n):
        if n <= 2:
            return n
        
        if self.__cache[n] != -1:
            return self.__cache[n]

        climb_1_step = self.__climbStairsRecursively(n - 1)
        climb_2_step = self.__climbStairsRecursively(n - 2)

        self.__cache[n] = climb_1_step + climb_2_step
        return self.__cache[n]
