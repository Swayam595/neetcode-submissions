class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.__climbStairsRecursively(n)

        # if n <= 2:
        #     return n
        # self.__cache = [-1] * (n + 1)
        # self.__climbStairsTopDown(n)
        # return self.__cache[n]

        return self.__climbStairsBottomUp(n)
    
    def __climbStairsRecursively(self, n):
        if n <= 2:
            return n

        climb_1_step = self.__climbStairsRecursively(n - 1)
        climb_2_step = self.__climbStairsRecursively(n - 2)

        return climb_1_step + climb_2_step

    def __climbStairsTopDown(self, n):
        if n <= 2:
            return n
        
        if self.__cache[n] != -1:
            return self.__cache[n]

        climb_1_step = self.__climbStairsTopDown(n - 1)
        climb_2_step = self.__climbStairsTopDown(n - 2)

        self.__cache[n] = climb_1_step + climb_2_step
        return self.__cache[n]

    def __climbStairsBottomUp(self, n):
        memo = [-1] * (n + 1)

        for i in range(1, n + 1):
            if i <= 2:
                memo[i] = i
            else:
                climb_1_step = memo[i - 1]
                climb_2_step = memo[i - 2]
                memo[i] = climb_1_step + climb_2_step
        
        return memo[n]