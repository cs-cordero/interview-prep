from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        best = 0
        running_total = 0
        seen = {}
        for i, num in enumerate(nums):
            if num == k:
                best = max(best, 1)

            running_total += num
            seen.setdefault(running_total, i)

            if running_total == k:
                best = max(best, i + 1)

            target = running_total - k
            earliest_seen_i = seen.get(target)
            if earliest_seen_i is not None:
                best = max(best, i - earliest_seen_i)
        return best


print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(Solution().maxSubArrayLen([-2, -1, 2, 1], 1))
print(Solution().maxSubArrayLen([1, 0, -1], -1))
