class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # return self.__merge_by_sorting(intervals)
        return self.__merge_by_greedy(intervals)

    # TC -> O(N + M)
    # SC -> O(M)
    # N -> len of the intervals array
    # M -> max start of the interval
    def __merge_by_greedy(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = max(interval[0] for interval in intervals)

        mp = [0] * (max_start + 1)

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

    # TC -> O(N * log(N) + N)
    # SC -> O(N)
    # N -> len of the intervals array
    def __merge_by_sorting(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][0] = min(ans[-1][0], intervals[i][0])
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans
