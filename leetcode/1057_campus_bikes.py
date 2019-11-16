from typing import List


class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        pairs = []

        for i, worker in enumerate(workers):
            r_worker, c_worker = worker
            for j, bike in enumerate(bikes):
                r_bike, c_bike = bike
                distance = abs(r_bike - r_worker) + abs(c_bike - c_worker)
                pairs.append((distance, i, j))

        assigned_workers = set()
        assigned_bikes = set()
        ans = [None for _ in range(len(workers))]
        for _, worker_index, bike_index in sorted(pairs):
            if worker_index in assigned_workers or bike_index in assigned_bikes:
                continue
            ans[worker_index] = bike_index
            assigned_workers.add(worker_index)
            assigned_bikes.add(bike_index)
        return ans
