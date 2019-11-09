from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)

        def helper(step: int) -> int:
            if step >= len(cost):
                return 0

            dp[step] = dp[step] or cost[step] + min(helper(step + 1), helper(step + 2))
            return dp[step]

        for i in range(len(cost) - 1, -1, -1):
            helper(i)
        return min(dp[0], dp[1])


print(Solution().minCostClimbingStairs([10, 15, 20]))
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
