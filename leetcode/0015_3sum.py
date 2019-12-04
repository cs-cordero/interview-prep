from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()

        def two_sum(start: int, target: int = 0) -> None:
            seen = set()
            for i in range(start, len(nums)):
                lookup = target - nums[i]
                if lookup in seen:
                    answer.add(tuple(sorted((0 - target, lookup, nums[i]))))
                seen.add(nums[i])

        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                continue
            seen.add(num)
            two_sum(i + 1, 0 - num)
        return answer
