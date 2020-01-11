from heapq import heappop, heappush
from typing import List


class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        heap = []
        for worker_index, worker in enumerate(workers):
            worker_x, worker_y = worker
            for bike_index, bike in enumerate(bikes):
                bike_x, bike_y = bike
                dist = abs(worker_x - bike_x) + abs(worker_y - bike_y)

                key = (dist, worker_index, bike_index)
                heappush(heap, key)

        result = [None for _ in range(len(workers))]
        assigned_bikes = set()
        while heap:
            _, worker_index, bike_index = heappop(heap)
            if result[worker_index] is not None or bike_index in assigned_bikes:
                continue
            assigned_bikes.add(bike_index)
            result[worker_index] = bike_index
        return result
