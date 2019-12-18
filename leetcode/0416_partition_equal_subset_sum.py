from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {0}
        for num in nums:
            dp = {dp_value + value for value in (num, -num) for dp_value in dp}
        return any(value == 0 for value in dp)
