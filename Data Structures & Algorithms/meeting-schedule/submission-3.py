"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals_sorted = sorted(intervals, key = lambda x: x.start)
        for i in range(1, len(intervals_sorted)):
            if intervals_sorted[i - 1].end > intervals_sorted[i].start:
                return False
        
        return True