from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(remaining: List[int], current: List[int]):
            if not remaining:
                return [current]

            results = []
            for i, num in enumerate(remaining):
                answers = helper(remaining[:i] + remaining[i + 1 :], current + [num])
                for answer in answers:
                    if answer in results:
                        continue
                    results.append(answer)
            return results

        return list(helper(nums, []))


print(Solution().permuteUnique([1, 1, 2]))
