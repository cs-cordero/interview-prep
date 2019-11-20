from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        best = 0
        for i in range(1, len(sorted_nums), 2):
            best += sorted_nums[i]
        return best
