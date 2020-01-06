from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == len(nums) - 1:
                return nums[0]
            elif nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            left_hand_is_sorted = nums[left] <= nums[mid]
            if left_hand_is_sorted:
                left = mid + 1
            else:
                right = mid - 1
