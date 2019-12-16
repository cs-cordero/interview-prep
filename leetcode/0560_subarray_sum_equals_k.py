from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping = defaultdict(int)
        mapping[0] = 1

        subarrays = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            subarrays += mapping[target]
            mapping[prefix_sum] += 1
        return subarrays
