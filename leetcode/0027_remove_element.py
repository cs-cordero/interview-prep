from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = len(nums) - 1
        read = 0
        if not nums:
            return 0

        while read <= write:
            while read <= write and nums[read] == val:
                nums[read], nums[write] = nums[write], nums[read]
                write -= 1
            read += 1
        return max(write + 1, 0)
