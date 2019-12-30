from typing import List


class interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def merge(intervals: List[interval]):
    merged = []
    if not intervals:
        return merged

    intervals.sort(key=lambda i: i.start)
    current_start = intervals[0].start
    current_end = intervals[0].end
    for interval in intervals[1:]:
        if interval.start <= current_end:
            current_end = max(current_end, interval.end)
        else:
            merged.append(type(interval)(current_start, current_end))
            current_start = interval.start
            current_end = interval.end
    merged.append(type(interval)(current_start, current_end))
    return merged
