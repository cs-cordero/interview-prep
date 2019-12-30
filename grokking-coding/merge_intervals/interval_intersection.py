from typing import List


def merge(
    intervals_a: List[List[int]], intervals_b: List[List[int]]
) -> List[List[int]]:
    result = []
    a = 0
    b = 0
    while a < len(intervals_a) and b < len(intervals_b):
        a_start, a_end = intervals_a[a]
        b_start, b_end = intervals_b[b]
        if a_start <= b_end and a_end >= b_start:
            result.append([max(a_start, b_start), min(a_end, b_end)])
        if a_end <= b_end:
            a += 1
        else:
            b += 1
    return result
