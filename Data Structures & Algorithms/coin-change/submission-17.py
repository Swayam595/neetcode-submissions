import sys
sys.setrecursionlimit(10000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min_coins = self.__recursive(0, coins, amount)
        # min_coins = self.__top_down(coins, amount)
        min_coins = self.__bottom_up(coins, amount)
        # min_coins = self.__bottom_up_optimized(coins, amount)

        return -1 if min_coins == float('inf') else min_coins
    
    # TC -> O(A * 2 ^ N)
    # SC -> O(A)
    # A -> Amount
    # N -> len of coins
    def __recursive(self, i: int, coins: List[int], amount: int) -> int | float('inf'):
        if amount == 0:
            return 0
        
        if i >= len(coins) or amount < 0:
            return float('inf')

        take = 1 + self.__recursive(i, coins, amount - coins[i])

        skip = self.__recursive(i + 1, coins, amount)

        return min(take, skip)

    # TC -> O(N * A)
    # SC -> O(N * A)
    # N -> Len of coins
    # A -> Amount
    def __top_down(self, coins: List[int], amount: int) -> int:
        cache = [[float('inf')] * (amount + 1) for _ in range(len(coins) + 1)]

        return self.__top_down_helper(0, coins, amount, cache)
    
    def __top_down_helper(self, i: int, coins: List[int], amount: int, cache: List[List[float]]) -> int | float:
        if amount == 0:
            return 0
        
        if amount < 0 or i >= len(coins):
            return float('inf')

        if cache[i][amount] != float('inf'):
            return cache[i][amount]

        take = float('inf')
        if coins[i] <= amount:
            take = 1 + self.__top_down_helper(i, coins, amount - coins[i], cache)
        skip = self.__top_down_helper(i + 1, coins, amount, cache)

        cache[i][amount] = min(take, skip)

        return cache[i][amount]

    # TC -> O(N * A)
    # SC -> O(N * A)
    # N -> Len of coins
    # A -> Amount
    def __bottom_up(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        M = amount

        dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 0

        for i in range(N - 1, -1, -1):
            for j in range(1, M  + 1):
                take = float('inf')
                if coins[i] <= j:
                    take = 1 + dp[i][j - coins[i]]
                skip = dp[i + 1][j]
                dp[i][j] = min(take, skip)

        return dp[0][M]
    
    def __bottom_up_optimized(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        M = amount

        dp = [float('inf')] * M
        dp[0] = 0

        for i in range(N - 1, -1, -1):
            new_dp = [float('inf')] * M
            for j in range(1, M + 1):
                take = float('inf')
                # if coins[i] <= j:
