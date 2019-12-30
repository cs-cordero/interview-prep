from heapq import heappop, heappush
from typing import List


class Meeting:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def min_meeting_rooms(meetings: List[Meeting]):
    heap = []
    min_rooms = 0
    meetings.sort(key=lambda meeting: meeting.start)
    for meeting in meetings:
        while heap and heap[0] <= meeting.start:
            heappop(heap)
        heappush(heap, meeting.end)
        min_rooms = max(min_rooms, len(heap))
    return min_rooms


print(min_meeting_rooms([Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]))
