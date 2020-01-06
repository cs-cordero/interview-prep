from heapq import heappop, heappush
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        positive_minheap = []
        negative_maxheap = []

        for num in nums:
            if num >= 0:
                heappush(positive_minheap, num)
            else:
                heappush(negative_maxheap, -num)
            while len(positive_minheap) > 3:
                heappop(positive_minheap)
            while len(negative_maxheap) > 3:
                heappop(negative_maxheap)

        six_nums = [-val for val in negative_maxheap] + positive_minheap
        best = float("-inf")
        for i in range(len(six_nums)):
            for j in range(i + 1, len(six_nums)):
                for k in range(j + 1, len(six_nums)):
                    best = max(best, six_nums[i] * six_nums[j] * six_nums[k])
        return best
