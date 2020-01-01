from heapq import heappop, heappush
from typing import List


class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


def find_next_interval(intervals: List[int]) -> List[int]:
    result = [-1] * len(intervals)
    starts = []
    ends = []
    for i, interval in enumerate(intervals):
        heappush(starts, (interval.start, i))
        heappush(ends, (interval.end, i))

    while starts and ends:
        current_end, current_i = heappop(ends)
        while starts and starts[0][0] < current_end:
            heappop(starts)
        if starts:
            result[current_i] = starts[0][1]

    return result
