from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    merged = []
    if not intervals:
        return merged

    i = 0
    new_start, new_end = new_interval
    start = float("inf")
    end = float("-inf")
    while i < len(intervals):
        current_start, current_end = intervals[i]
        if new_start <= current_end and new_end >= current_start:
            start = min(new_start, current_start)
            end = max(new_end, current_end)
        else:
            start, end = intervals[i]

        while i < len(intervals):
            current_start, current_end = intervals[i]
            if not (current_start <= end and current_end >= start):
                break
            start = min(start, current_start)
            end = max(end, current_end)
            i += 1
        merged.append([start, end])
    return merged


print(insert([[1, 3], [5, 7], [8, 12]], [4, 10]))
