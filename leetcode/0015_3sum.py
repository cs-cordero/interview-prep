from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i, num in enumerate(nums):
            for sub_result in two_sum(nums, -num, i + 1, len(nums) - 1):
                result.add(tuple(sorted([num, *sub_result])))
        return list(result)


def two_sum(
    nums: List[int], target: int, left: int, right: int
) -> List[Tuple[int, int]]:
    seen = set()
    result = set()
    for i in range(left, right + 1):
        k = target - nums[i]
        if k in seen:
            result.add((k, nums[i]))
        seen.add(nums[i])
    return list(result)
