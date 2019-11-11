from heapq import heappop, heappush
from typing import List


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], K: int
    ) -> float:
        heap = []
        best = float("inf")
        total_quality = 0

        ratios = [(w / q, q, w) for w, q in zip(wage, quality)]
        for ratio, quality, wage in sorted(ratios):
            heappush(heap, -quality)
            total_quality += quality
            if len(heap) > K:
                total_quality += heappop(heap)
            elif len(heap) < K:
                continue

            best = min(best, wage / (quality / total_quality))
        return best


print(Solution().mincostToHireWorkers([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3))
