import heapq
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        heapq.heapify(nums2)
        i = 0
        while nums2:
            if nums1[i] > nums2[0] or i >= m:
                if i < m:
                    smallest = heapq.heappushpop(nums2, nums1[i])
                else:
                    smallest = heapq.heappop(nums2)
                nums1[i] = smallest
            i += 1
