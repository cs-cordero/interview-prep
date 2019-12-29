from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0

        start = 0
        current = 1
        for end, value in enumerate(nums):
            current *= value
            while start < end and current >= k:
                current /= nums[start]
                start += 1

            if current < k:
                result += end - start + 1

        return result


assert (
    Solution().numSubarrayProductLessThanK([10, 2, 2, 5, 4, 4, 4, 3, 7, 7], 289) == 31
)
