from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 0
        current = float("-inf")
        for read, num in enumerate(nums):
            if num > current:
                current = num
                nums[write] = num
                write += 1
        return write
