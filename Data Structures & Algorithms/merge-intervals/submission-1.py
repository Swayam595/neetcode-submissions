class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # return self.__merge_by_sorting(intervals)
        return self.__merge_by_greedy(intervals)

    # TC -> O(N * log(N))
    # SC -> O(N)
    # N -> len of intervals array
    # O(1) or O(n) SC depending on the sorting algorithm
    def __merge_by_greedy(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)

        mp = [0] * (max_val + 1)
        for start, end in intervals:
            mp[start] = max(end + 1, mp[start])

        ans = []
        have = -1
        interval_start = -1

        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i] - 1, have)
            
            if have == i:
                ans.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            ans.append([interval_start, have])

        return ans

    # TC -> O(N * log(N))
    # SC -> O(N)
    # N -> len of intervals array
    # O(1) or O(n) SC depending on the sorting algorithm
    def __merge_by_sorting(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])

        ans = []
        ans.append(intervals[0])

        for i in range(1, len(intervals)):
            if self.__is_overlapping(ans[-1], intervals[i]):
                ans[-1][0] = min(ans[-1][0], intervals[i][0])
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans
    
    def __is_overlapping(self, interval1: List[int], interval2: List[int]) -> bool:
        return interval1[1] >= interval2[0]