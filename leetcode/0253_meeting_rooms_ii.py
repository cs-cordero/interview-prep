from heapq import heappop, heappush
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []

        rooms_needed = 0
        for start, end in sorted(intervals):
            while heap and start >= heap[0]:
                heappop(heap)
            heappush(heap, end)
            rooms_needed = max(rooms_needed, len(heap))
        return rooms_needed
