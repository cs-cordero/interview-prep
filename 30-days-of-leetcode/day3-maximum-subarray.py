from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Given an integer array nums, find the contiguous subarray (containing
        # at least one number) which has the largest sum and return its sum.
        result = float("-inf")

        current_sum = 0
        for num in nums:
            current_sum = max(current_sum + num, num)
            result = max(result, current_sum)

        return max(result, current_sum)
