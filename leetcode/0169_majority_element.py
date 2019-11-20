from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        limit = len(nums) // 2
        for number, count in counter.items():
            if count > limit:
                return number
