from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        current = 1
        for i in range(1, len(nums)):
            current *= nums[i - 1]
            result[i] *= current

        current = 1
        for i in range(len(nums) - 2, -1, -1):
            current *= nums[i + 1]
            result[i] *= current

        return result
