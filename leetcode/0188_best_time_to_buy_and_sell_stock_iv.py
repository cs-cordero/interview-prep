from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        if k >= len(prices) // 2:
            return max_profit_no_limit(prices)

        dp = [[0 for _ in range(len(prices))] for _ in range(2)]

        t = 0
        for t in range(1, k + 1):
            best_buy_profit = dp[(t - 1) % 2][0] - prices[0]
            for i in range(1, len(prices)):
                dp[t % 2][i] = max(dp[t % 2][i - 1], prices[i] + best_buy_profit)
                best_buy_profit = max(best_buy_profit, dp[(t - 1) % 2][i] - prices[i])
        return dp[t % 2][-1]


def max_profit_no_limit(prices: List[int]) -> int:
    if not prices:
        return 0

    profit = 0
    prev = prices[0]
    for price in prices:
        if price > prev:
            profit += price - prev
        prev = price
    return profit


print(Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]))
