from typing import List, Tuple


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            return 0 if nums[0] == target else -1

        left, right = self.find_pivot_points(nums)
        while left != right and right >= 0 and left <= (len(nums) - 1):
            if right < left:
                distance_from_l_to_r = right + (len(nums) - left)
            else:
                distance_from_l_to_r = right - left
            mid = (left + (distance_from_l_to_r // 2)) % len(nums)
            if left == mid or right == mid:
                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                break

            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1

    def find_pivot_points(self, nums: List[int]) -> Tuple[int, int]:
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return left, right

        while left < right - 1:
            mid = (right + left) // 2
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid
        return right, left


assert Solution().search([4, 5, 6, 7, 0, 1, 2], 1) == 5
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert Solution().search([], 3) == -1
assert Solution().search([1], 3) == -1
assert Solution().search([1], 1) == 0
assert Solution().search([1, 3], 1) == 0
assert Solution().search([1, 3], 3) == 1
assert Solution().search([3, 5, 1], 3) == 0
