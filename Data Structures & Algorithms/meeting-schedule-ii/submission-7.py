"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)
        Minheap = []
        for interval in intervals:
            if Minheap and Minheap[0] <= interval.start:
                heapq.heappop(Minheap)
            heapq.heappush(Minheap, interval.end)
        return len(Minheap)