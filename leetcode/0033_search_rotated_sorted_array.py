from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1

        pivot_point = None
        if nums[0] < nums[-1]:
            pivot_point = len(nums) - 1
        else:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                    pivot_point = mid
                    break

                if nums[0] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        assert pivot_point is not None

        left = 0
        right = len(nums) - 1
        if target > nums[pivot_point]:
            return -1
        elif target <= nums[pivot_point] and nums[0] <= target:
            right = pivot_point
        elif target < nums[0]:
            left = pivot_point + 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


"""
7, 1, 2, 3, 4, 5, 6
2, 3, 4, 5, 6, 7, 1
"""
