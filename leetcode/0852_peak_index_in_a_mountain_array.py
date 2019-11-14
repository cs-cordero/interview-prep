from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        best = None
        highest = float("-inf")
        for index, value in enumerate(A):
            if value > highest:
                highest = max(value, highest)
                best = index
        return best
