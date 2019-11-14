from bisect import bisect, bisect_left
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [bisect_left(nums, target), max(bisect(nums, target) - 1, 0)]
        return [
            val if val < len(nums) and nums[val] == target else -1 for val in result
        ]
