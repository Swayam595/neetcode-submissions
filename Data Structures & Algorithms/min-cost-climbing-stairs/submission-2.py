class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # return min(
        #     self.__min_cost_climbing_stairs_recursive(0, cost), 
        #     self.__min_cost_climbing_stairs_recursive(1, cost)
        # )
        # return self.__min_cost_climbing_stairs_topdown(cost)
        # return self.__min_cost_climbing_stairs_bottomup(cost)
        return self.__min_cost_climbing_stairs_bottomup_optimised(cost)

    def __min_cost_climbing_stairs_bottomup_optimised(self, cost: List[int]) -> int:
        n = len(cost)
        take_1step = 0
        take_2step = 0

        for i in range(2, n + 1):
            take_n_step = min(
                take_1step + cost[i - 1],
                take_2step + cost[i - 2]
            )
            
            take_2step = take_1step
            take_1step = take_n_step

        return take_n_step

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of the cost list
    def __min_cost_climbing_stairs_bottomup(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )
        return dp[n]

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of the cost list
    def __min_cost_climbing_stairs_topdown(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 1)
        
        return min(
            self.__min_cost_climbing_stairs_topdown_helper(0, memo, cost),
            self.__min_cost_climbing_stairs_topdown_helper(1, memo, cost)
        )

    def __min_cost_climbing_stairs_topdown_helper(self, i: int, memo: List[int], cost: List[int]) -> int:
        if i >= len(cost):
            return 0
        
        if memo[i] != 0:
            return memo[i]
        
        take_1step = self.__min_cost_climbing_stairs_topdown_helper(i + 1, memo, cost)
        take_2step = self.__min_cost_climbing_stairs_topdown_helper(i + 2, memo, cost)

        memo[i] = cost[i] + min(take_1step, take_2step)
        return memo[i]

    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> len of the cost list
    def __min_cost_climbing_stairs_recursive(self, i: int, cost: List[int]) -> int:
        if i >= len(cost):
            return 0
        
        take_1step = self.__min_cost_climbing_stairs_recursive(i + 1, cost)
        take_2step =  self.__min_cost_climbing_stairs_recursive(i + 2, cost)

        return cost[i] + min(take_1step, take_2step)