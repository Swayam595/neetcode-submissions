class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # min_coins_needed = self.__recursive(0, coins, amount)
        # min_coins_needed = self.__topDown(coins, amount)

        min_coins_needed = self.__bottomUp(coins, amount)

        return min_coins_needed if min_coins_needed != float('inf') else -1
        
    def __recursive(self, i: int, coins: List[int], amount: int) -> int | float('inf'):
        if amount == 0:
            return 0

        if i == len(coins) or amount < 0:
            return float('inf')
        
        take = 1 + self.__recursive(i, coins, amount - coins[i])
        
        skip = self.__recursive(i + 1, coins, amount)

        return min(take, skip)
    
    def __topDown(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        M = amount
        memo = [[float('inf')] * (M + 1) for _ in range(N + 1)]

        return self.__topDownHelper(0, coins, amount, memo)
    
    def __topDownHelper(self, i: int, coins: List[int], amount: int, memo: List[List[int]]) -> int | float('inf'):
        if amount == 0:
            return 0
        
        if i == len(coins) or amount < 0:
            return float('inf')
        
        if memo[i][amount] != float('inf'):
            return memo[i][amount]
        
        take = 1 + self.__topDownHelper(i, coins, amount - coins[i], memo)
        skip = self.__topDownHelper(i + 1, coins, amount, memo)

        memo[i][amount] = min(take, skip)

        return memo[i][amount]

    def __bottomUp(self, coins: List[int], amount: int) -> int | float('inf'):
        N = len(coins)
        M = amount

        dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for j in range(M + 1):
                if j == 0:
                    dp[i][j] = 0
                else:
                    take = float('inf')
                    if coins[i] <= amount:
                        take = 1 + dp[i][j - coins[i]]
                    skip = dp[i + 1][j]
                    dp[i][j] = min(take, skip)
                    
        return dp[0][M]