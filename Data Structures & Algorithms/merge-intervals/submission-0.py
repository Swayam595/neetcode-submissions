class Solution:
    # TC -> O(N * log(N))
    # SC -> O(N)
    # N -> len of intervals array
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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