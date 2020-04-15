from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            num = nums[fast]
            if num != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
