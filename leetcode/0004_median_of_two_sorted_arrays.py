from bisect import bisect_left
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 and not nums2:
            nums2 = nums1
        elif nums2 and not nums1:
            nums1 = nums2

        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            target_indexes = [total_length // 2, total_length // 2 - 1]
        else:
            target_indexes = [total_length // 2]

        def find_value_at_true_index(i: int) -> int:
            num1_ptr = 0
            num1_true_offset = 0
            left = 0
            right = len(nums2) - 1
            while left <= right:
                mid = (left + right) // 2
                value = nums2[mid]
                bisection_point = bisect_left(nums1, value)
                true_index = mid + bisection_point
                if true_index == i:
                    return nums2[mid]
                elif true_index < i:
                    left = mid + 1
                    num1_ptr = bisection_point
                    num1_true_offset = true_index + 1
                else:
                    right = mid - 1
            return nums1[num1_ptr:][i - num1_true_offset]

        values_at_targets = [find_value_at_true_index(i) for i in target_indexes]
        if len(values_at_targets) == 2:
            return sum(values_at_targets) / 2
        return float(values_at_targets[0])


print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5], [3, 4]))
print(Solution().findMedianSortedArrays([3], [-2, -1]))
