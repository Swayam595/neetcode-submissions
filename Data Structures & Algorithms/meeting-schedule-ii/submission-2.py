"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # TC -> O(N * log(N))
    # SC -> O(N)
    # N -> len of intervals array
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key = lambda x: x.start)
        meeting_rooms = [intervals[0].end]

        for interval in intervals[1:]:
            if meeting_rooms[0] <= interval.start:
                heapq.heappop(meeting_rooms)
            heapq.heappush(meeting_rooms, interval.end)
        return len(meeting_rooms)
