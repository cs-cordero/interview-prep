from heapq import heappop, heappush
from typing import List


class job:
    def __init__(self, start: int, end: int, cpu_load: int) -> None:
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


def find_max_cpu_load(jobs: List[job]):
    current_cpu_load = 0
    max_cpu_load = 0
    heap = []

    jobs.sort(key=lambda j: j.start)
    for _job in jobs:
        while heap and heap[0][0] <= _job.start:
            _, cpu_load_reduction = heappop(heap)
            current_cpu_load -= cpu_load_reduction
        heappush(heap, (_job.end, _job.cpu_load))
        current_cpu_load += _job.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load
