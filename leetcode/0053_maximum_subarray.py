from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        best = nums[0]
        current = nums[0]
        for i, num in enumerate(nums[1:], 1):
            current += num
            if num > current:
                current = num
            best = max(best, current)
        return best
