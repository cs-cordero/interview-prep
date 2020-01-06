from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        current_buy = float("inf")
        for price in prices:
            if price < current_buy:
                current_buy = price
            best_profit = max(best_profit, price - current_buy)
        return best_profit
