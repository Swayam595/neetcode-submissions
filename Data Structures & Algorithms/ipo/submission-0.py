class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        return self.__findMaximizedCapitalTwoHeap(k, w, profits, capital)
    
    def __findMaximizedCapitalTwoHeap(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = []
        min_capital = [[capital[i], profits[i]] for i in range(len(capital))]

        heapq.heapify(min_capital)

        for _ in range(k):
            while len(min_capital) > 0 and min_capital[0][0] <= w:
                capital, profit = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -profit)
            
            if len(max_profit) == 0:
                break

            curr_job_profit = -1 * heapq.heappop(max_profit)
            w += curr_job_profit
        
        return w