from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if not prices:
            return max_profit

        buy = prices[0]
        for price in prices[1:]:
            buy = min(buy, price)
            max_profit = max(max_profit, price - buy)
        return max_profit
