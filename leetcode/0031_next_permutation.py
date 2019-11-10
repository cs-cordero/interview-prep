from typing import List


def reverse_in_place(nums: List[int], left: int, right: int) -> None:
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        best_i = None
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                best_i = max(best_i, i) if best_i else i

        if best_i is None:
            reverse_in_place(nums, 0, len(nums) - 1)
            return None

        best_j = best_i + 1
        for j in range(best_i + 1, len(nums)):
            if nums[best_i] < nums[j]:
                best_j = j

        nums[best_i], nums[best_j] = nums[best_j], nums[best_i]

        reverse_in_place(nums, best_i + 1, len(nums) - 1)
