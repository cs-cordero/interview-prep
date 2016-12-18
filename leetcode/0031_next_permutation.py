from typing import List


def reverse_in_place(nums: List[int], left: int = 0, right: int = None):
    if not right:
        right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivot = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                pivot = i - 1

        if pivot is None:
            nums.reverse()
            return

        next_greater = pivot + 1
        for j in range(next_greater + 1, len(nums)):
            if nums[j] > nums[pivot] and nums[j] <= nums[next_greater]:
                next_greater = j

        nums[pivot], nums[next_greater] = nums[next_greater], nums[pivot]
        reverse_in_place(nums, pivot + 1)
