from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            k = target - num
            if k in hashmap:
                return [hashmap[k], i]
            hashmap[num] = i
        return []
