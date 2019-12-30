from typing import List


def can_attend_all_appointments(intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda i: i[0])

    prev_start, prev_end = float("inf"), float("-inf")
    for start, end in intervals:
        if start <= prev_end and end >= prev_start:
            return False
        prev_start = start
        prev_end = end
    return True
