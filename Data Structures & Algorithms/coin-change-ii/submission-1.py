class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # return self.__recursive(0, amount, coins)
        return self.__topDown(amount, coins)

    def __recursive(self, i: int, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        
        if i == len(coins) or amount < 0:
            return 0
        
        take = self.__recursive(i, amount - coins[i], coins)
        skip = self.__recursive(i + 1, amount, coins)

        return take + skip

    def __topDown(self, amount: int, coins: list[int]) -> int:
        N = len(coins)
        M = amount
        memo = [[0] * (M + 1) for _ in range(N + 1)]

        return self.__topDownHelper(0, amount, coins, memo)

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