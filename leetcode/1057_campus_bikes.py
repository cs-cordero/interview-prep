from typing import List


class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        sorted_distances = sorted(
            (abs(by - wy) + abs(bx - wx), wi, bi)
            for wi, (wx, wy) in enumerate(workers)
            for bi, (bx, by) in enumerate(bikes)
        )

        result = [None for _ in range(workers)]
        assigned_bikes = set()
        for _, w, b in sorted_distances:
            if result[w] is not None or b in assigned_bikes:
                continue

            assigned_bikes.add(b)
            result[w] = b
            if len(assigned_bikes) == len(bikes):
                # all bikes assigned
                break
        return result
