from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prev_max, current_max = nums[0]
        prev_min, current_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            current_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])
            prev_min, prev_max = current_min, current_max
            global_max = max(global_max, current_max, current_min)
        return global_max
