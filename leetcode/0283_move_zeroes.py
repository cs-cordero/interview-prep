from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1


data = [0, 1, 0, 3, 12]
Solution().moveZeroes(data)
assert data == [1, 3, 12, 0, 0]
