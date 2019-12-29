from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        for start in range(len(nums)):
            current = 1
            for end in range(start, len(nums)):
                current *= nums[end]
                if current < k:
                    result += 1
                else:
                    break
        return result


print(Solution().numSubarrayProductLessThanK([10, 2, 2, 5, 4, 4, 4, 3, 7, 7], 289))
