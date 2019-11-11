from heapq import heappop, heappush
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        if not points or K <= 0:
            return heap

        for i, (x, y) in enumerate(points):
            distance = x ** 2 + y ** 2
            heappush(heap, (-distance, i))
            if len(heap) > K:
                heappop(heap)
        return [points[index] for _, index in heap]
