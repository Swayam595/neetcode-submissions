class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.__max_profit_brute_force(prices)
        return self.__max_profit_optimized(prices)
    
    # TC -> O(N)
    # SC -> O(1)
    # N -> len of prices
    def __max_profit_optimized(self, prices: List[int]) -> int:
        max_profit = 0
        curr_price = float('inf')

        for price in prices:
            max_profit = max(max_profit, price - curr_price)
            curr_price = min(curr_price, price)
        
        return max_profit

    # TC -> O(N ^ 2)
    # SC -> O(1)
    # N -> len of prices
    def __max_profit_brute_force(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                max_profit = max(max_profit, prices[j] - prices[i])
        
        return max_profit