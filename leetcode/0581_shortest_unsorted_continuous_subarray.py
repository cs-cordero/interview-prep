from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        begin = None
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                begin = i - 1
                break

        if begin is None:
            return 0

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < nums[i - 1]:
                end = i
                break

        min_in_window = min(nums[begin : end + 1])
        max_in_window = max(nums[begin : end + 1])

        for leftmost in range(begin + 1):
            if nums[leftmost] > min_in_window:
                begin = leftmost
                break

        for rightmost in range(len(nums) - 1, end - 1, -1):
            if nums[rightmost] < max_in_window:
                end = rightmost
                break

        return end - begin + 1
