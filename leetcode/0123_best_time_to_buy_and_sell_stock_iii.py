from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [[0 for _ in range(len(prices))] for _ in range(3)]

        for k in range(1, 3):
            best_rebuy_amount = dp[k - 1][0] - prices[0]
            for i in range(1, len(prices)):
                dp[k][i] = max(0, dp[k][i - 1], prices[i] + best_rebuy_amount)
                best_rebuy_amount = max(best_rebuy_amount, dp[k - 1][i] - prices[i])

        return dp[-1][-1]


Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
