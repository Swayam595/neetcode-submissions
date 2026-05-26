class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # return self.__recursive(0, days, costs)
        # return self.__topDown(days, costs)
        return self.__bottomUp(days, costs)
    
    # TC - O(3^N)
    # SC - O(N)
    def __recursive(self, i: int, days:List[int], costs: List[int]) -> int:
        if i == len(days):
            return 0
        
        take_1_day_pass = costs[0] + self.__recursive(i + 1, days, costs)

        j = i
        while j < len(days) and days[j] < days[i] + 7:
            j += 1
        
        take_7_day_pass = costs[1] + self.__recursive(j, days, costs)

        k = i
        while k < len(days) and days[k] < days[i] + 30:
            k += 1
        
        take_30_day_pass = costs[2] + self.__recursive(k, days, costs)

        return min(take_1_day_pass, take_7_day_pass, take_30_day_pass)
    
    # TC - O(3 * N)
    # SC - O(2 * N)
    def __topDown(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        memo = [-1] * (N + 1)

        return self.__topDownHelper(0, days, costs, memo)

    def __topDownHelper(self, i: int, days: List[int], costs: List[int], memo: List[int]) -> int:
        if i == len(days):
            return 0
        
        if memo[i] != -1:
            return memo[i]

        take_1_day_pass = costs[0] + self.__recursive(i + 1, days, costs)

        j = i
        while j < len(days) and days[j] < days[i] + 7:
            j += 1
        
        take_7_day_pass = costs[1] + self.__recursive(j, days, costs)

        k = i
        while k < len(days) and days[k] < days[i] + 30:
            k += 1
        
        take_30_day_pass = costs[2] + self.__recursive(k, days, costs)

        memo[i] = min(take_1_day_pass, take_7_day_pass, take_30_day_pass)

        return memo[i]

    # TC - O(N * 3)
    # SC - O(N)
    def __bottomUp(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        dp = [0] * (N + 1)

        for i in range(N - 1, -1, -1):
            take_1_day_pass = costs[0] + dp[i + 1]

            j = i
            while j < N and days[j] < days[i] + 7:
                j += 1
            
            take_7_day_pass = costs[1] + dp[j]

            k = i
            while k < N and days[k] < days[i] + 30:
                k += 1
            
            take_30_day_pass = costs[2] + dp[k]

            dp[i] = min(take_1_day_pass, take_7_day_pass, take_30_day_pass)

        return dp[0]