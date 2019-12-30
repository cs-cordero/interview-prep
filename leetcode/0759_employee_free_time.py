from heapq import heappop, heappush
from typing import List


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        result = []
        heap = []
        for i, employee in enumerate(schedule):
            interval = employee[0]
            heappush(heap, (interval.start, i, 0))

        start, end = None, None
        while heap:
            _, employee_id, employee_index = heappop(heap)

            employee = schedule[employee_id]
            next_index = employee_index + 1
            if next_index < len(employee):
                heappush(heap, (employee[next_index].start, employee_id, next_index))

            interval = employee[employee_index]
            if start is None and end is None:
                start = interval.start
                end = interval.end
            elif interval.start <= end and interval.end > start:
                start = min(start, interval.start)
                end = max(end, interval.end)
            else:
                result.append(Interval(end, interval.start))
                start = interval.start
                end = interval.end

        return result
