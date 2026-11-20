class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.__merge_by_sorting(intervals)

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
