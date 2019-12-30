from heapq import heappop, heappush
from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end="")


def find_employee_free_time(schedule: List[List[Interval]]):
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


for interval in find_employee_free_time(
    [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
):
    interval.print_interval()
    print()
