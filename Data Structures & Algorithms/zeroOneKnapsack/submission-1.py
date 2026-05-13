class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # return self.__recursion(0, profit, weight, capacity)
        return self.__topDown(profit, weight, capacity)
    
    # TC - O(2^n) 
    # SC - O(n) -> Depth of the recursion stack
    def __recursion(self, i: int, profit: List[int], weight: List[int], capacity: int) -> int:        
        if i == len(profit):
            return 0
        
        skip = self.__recursion(i + 1, profit, weight, capacity)
        take = 0
        if weight[i] <= capacity:
            take = profit[i] + self.__recursion(i + 1, profit, weight, capacity - weight[i])

        return max(take, skip)

    def __topDown(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity

        cache = [[-1] * (M + 1) for _ in range(N + 1)]
        self.__topDownHelper(0, profit, weight, capacity, cache)
        
        return cache[0][M]
    
    def __topDownHelper(self, i: int, profit: List[int], weight: List[int], capacity: int, cache: List[List[int]]) -> int:
        if i == len(profit):
            return 0
        
        if cache[i][capacity] != -1:
            return cache[i][capacity]
        
        skip = self.__topDownHelper(i + 1, profit, weight, capacity, cache)
        take = 0

        if weight[i] <= capacity:
            take = profit[i] + self.__topDownHelper(i + 1, profit, weight, capacity - weight[i], cache)
        cache[i][capacity] = max(take, skip)

        return cache[i][capacity]
