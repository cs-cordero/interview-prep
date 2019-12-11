from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for value, count in counts.items():
            heappush(heap, (count, value))
            while len(heap) > k:
                heappop(heap)
        return [value for _, value in heap]
