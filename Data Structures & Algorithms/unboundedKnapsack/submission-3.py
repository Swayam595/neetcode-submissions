class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # return self.__recursive(0, profit, weight, capacity)
        # return self.__topDown(profit, weight, capacity)
        # return self.__bottomUp(profit, weight, capacity)
        return self.__bottomUpOptimized(profit, weight, capacity)
    
    # TC - O(2 ^ Capacity)
    # SC - O(Capacity)
    def __recursive(self, i: int, profit: List[int], weight: List[int], capacity: int) -> int:
        if i == len(profit):
            return 0
        
        take = 0
        if weight[i] <= capacity:
            take = profit[i] + self.__recursive(i, profit, weight, capacity - weight[i])
        
        skip = self.__recursive(i + 1, profit, weight, capacity)

        return max(take, skip)

    # TC - O(N * Capacity)
    # SC - O(N * Capacity + Capacity)
    def __topDown(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity
        memo = [[0] * (M + 1) for _ in range(N + 1)]

        return self.__topDownHelper(0, profit, weight, capacity, memo)

    # TC - O(N * Capacity)
    # SC - O(Capacity)
    def __topDownHelper(self, i: int, profit: List[int], weight: List[int], capacity: int, memo: List[List[int]]) -> int:
        if i == len(profit):
            return 0
        
        if memo[i][capacity] != 0:
            return memo[i][capacity]
        
        take = 0
        if weight[i] <= capacity:
            take = profit[i] + self.__recursive(i, profit, weight, capacity - weight[i])
        
        skip = self.__recursive(i + 1, profit, weight, capacity)

        memo[i][capacity] = max(take, skip)
        
        return memo[i][capacity]

    # TC - O(N * Capacity)
    # SC - O(N * Capacity)
    def __bottomUp(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for j in range(M + 1):
                take = 0
                if weight[i] <= j:
                    take = profit[i] + dp[i][j - weight[i]]
                skip = dp[i + 1][j]
                dp[i][j] = max(take, skip)
        
        return dp[0][M]

    # TC - O(N * Capacity)
    # SC - O(Capacity)
    def __bottomUpOptimized(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity
        dp = [0] * (M + 1)

        for i in range(N - 1, -1, -1):
            new_dp = [0] * (M + 1)
            for j in range(M + 1):
                take = 0
                if weight[i] <= j:
                    take = profit[i] + new_dp[j - weight[i]]

                skip = dp[j]
                new_dp[j] = max(take, skip)

            dp = new_dp
        
        return dp[M]
