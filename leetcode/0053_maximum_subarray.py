from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current = nums[0]
        best = current

        for num in nums[1:]:
            if num > current + num:
                current = num
            else:
                current += num
            best = max(best, current)
        return best
