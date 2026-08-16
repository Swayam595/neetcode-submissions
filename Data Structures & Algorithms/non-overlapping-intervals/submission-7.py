class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: interval[0])

        # return len(intervals) - self.__recursion(0, -1, intervals)
        # return len(intervals) - self.__top_down(intervals)
        # return len(intervals) - self.__bottom_up(intervals)
        return self.__greedy(intervals)

    # TC -> O(N * log(N))
    # SC -> O(N) or O(1) based on sorting algorithm
    # N -> Len of intervals array    
    def __greedy(self, intervals: List[List[int]]) -> int:
        ans = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                ans += 1
                prev_end = min(prev_end, end)

        return ans

    # TC -> O(N ^ 2)
    # SC -> O(N)
    # N -> Len of intervals array    
    def __bottom_up(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        dp = [0] * n

        for i in range(n):
            dp[i] = 1
            for j in range(i):
                take = 0
                if intervals[j][1] <= intervals[i][0]:
                    take = 1 + dp[j]
                skip = dp[i]
                dp[i] = max(take, skip)
        
        return dp[n - 1]
    
    # TC -> O(N ^ 2)
    # SC -> O(N ^ 2)
    # N -> Len of intervals array
    def __top_down(self, intervals: List[List[int]]) -> int:
        cache = [[-1] * len(intervals) for _ in range(len(intervals))]

        return self.__top_down_helper(0, -1, intervals, cache)
    
    def __top_down_helper(self, i: int, prev: int, intervals: List[List[int]], cache: List[List[int]]) -> int: 
        if i >= len(intervals):
            return 0
        
        if cache[i][prev] != -1:
            return cache[i][prev]
        
        take = 0
        if prev == -1 or intervals[prev][1] <= intervals[i][0]:
            take = 1 + self.__top_down_helper(i + 1, i, intervals, cache)
        
        skip = self.__top_down_helper(i + 1, prev, intervals, cache)
        
        cache[i][prev] = max(take, skip)
        return cache[i][prev]


    # TC -> O(2 ^ N)
    # SC -> O(N)
    # N -> Len of intervals array
    def __recursion(self, i: int, prev: int, intervals: List[List[int]]) -> int:
        if i >= len(intervals):
            return 0

        take = 0
        if prev == -1 or intervals[prev][1] <= intervals[i][0]:
            take = 1 + self.__recursion(i + 1, i, intervals)

        skip = self.__recursion(i + 1, prev, intervals)

        return max(take, skip)
        
        