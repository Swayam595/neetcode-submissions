class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # return self.__brute_force(intervals, newInterval)
        # return self.__linear_search(intervals, newInterval)
        return self.__greedy(intervals, newInterval)

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of intervals array
    def __greedy(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        ans.append(newInterval)
        return ans

    # TC -> O(N)
    # SC -> O(1)
    # N -> len of intervals array
    def __linear_search(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        ans = []

        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        ans.append(newInterval)

        while i < n:
            ans.append(intervals[i])
            i += 1
        
        return ans

    # TC -> O(N)
    # SC -> O(N)
    # N -> len of intervals array
    # not optimized because of extra space used to store intervals after merge
    # and 2 passes one for merging and 2nd to remove overlap
    def __brute_force(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        elif not newInterval:
            return intervals
        elif newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        elif intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]

        intervals_after_merge = self.__insert_in_between(intervals, newInterval)
        return self.__merge_overlapping_intervals(intervals_after_merge)

    def __insert_in_between(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        is_added = False

        for i in range(n):
            if is_added:
                ans.append(intervals[i])
            else:
                if intervals[i][0] >= newInterval[0]:
                    ans.append(newInterval)
                    is_added = True
                ans.append(intervals[i])
        
        if not is_added:
            ans.append(newInterval)
            
        return ans
    def __merge_overlapping_intervals(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        for interval in intervals:
            if ans and ans[-1][1] >= interval[0]:
                ans[-1][0] = min(ans[-1][0], interval[0])
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval) 

        return ans
