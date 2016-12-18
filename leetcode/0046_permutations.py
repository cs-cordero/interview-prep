from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(remaining: List[int], current: List[int]):
            if not remaining:
                return [current]

            results = []
            for i, num in enumerate(remaining):
                results.extend(
                    helper(remaining[:i] + remaining[i + 1 :], current + [num])
                )
            return results

        return helper(nums, [])


print(Solution().permute([1, 2, 3]))
