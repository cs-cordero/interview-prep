from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Given a non-empty array of integers, every element appears twice
        # except for one. Find that single one.
        result = 0
        for num in nums:
            result ^= num
        return result
