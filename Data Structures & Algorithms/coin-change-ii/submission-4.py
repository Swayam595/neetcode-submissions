class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # return self.__recursive(0, amount, coins)
        # return self.__topDown(amount, coins)
        return self.__bottomUpOpmizied(amount, coins)

    # TC - O(2 ^ max(N, A / m))
    # SC - O(N)
    ## Where N is the number of coins, A is the given amount and m is the minimum value among all the coins.
    def __recursive(self, i: int, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        
        if i == len(coins) or amount < 0:
            return 0
        
        take = self.__recursive(i, amount - coins[i], coins)
        skip = self.__recursive(i + 1, amount, coins)

        return take + skip

    # TC - O(N * A)
    # SC - O(N * A + N)
    # Where N is the number of coins, A is the given amount
    def __topDown(self, amount: int, coins: list[int]) -> int:
        N = len(coins)
        M = amount
        memo = [[0] * (M + 1) for _ in range(N + 1)]

        return self.__topDownHelper(0, amount, coins, memo)

    # TC - O(N * A)
    # SC - O(N)
    # Where N is the number of coins, A is the given amount
    def __topDownHelper(self, i: int, amount: int, coins: List[int], memo: List[List[int]]) -> int:
        if amount == 0:
            return 1
        
        if i == len(coins) or amount < 0:
            return 0
        
        if memo[i][amount] != 0:
            return memo[i][amount]
        
        take = self.__topDownHelper(i, amount - coins[i], coins, memo)
        skip = self.__topDownHelper(i + 1, amount, coins, memo)

        memo[i][amount] = take + skip

        return memo[i][amount]

    # TC - O(N * A)
    # SC - O(N * A)
    # Where N is the number of coins, A is the given amount
    def __bottomUp(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        M = amount

        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(N - 1, -1, -1):
            for j in range(M + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    take = dp[i][j - coins[i]] if j - coins[i] >= 0 else 0
                    skip = dp[i + 1][j]
                    dp[i][j] = take + skip
        
        return dp[0][M]

    # TC - O(N * A)
    # SC - O(N)
    # Where N is the number of coins, A is the given amount
    def __bottomUpOpmizied(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        M = amount

        dp = [0] * (M + 1)

        for i in range(N - 1, -1, -1):
            new_dp = [0] * (M + 1)
            for j in range(M + 1):
                if j == 0:
                    new_dp[j] = 1
                else:
                    take = new_dp[j - coins[i]] if j - coins[i] >= 0 else 0
                    skip = dp[j]
                    new_dp[j] = take + skip
            dp = new_dp
        
        return dp[M]