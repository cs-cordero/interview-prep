from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        buy_price = prices[0]
        current_profit = 0
        for i in range(1, len(prices)):
            price = prices[i]
            if price < prices[i - 1]:
                max_profit += current_profit
                current_profit = 0
                buy_price = price
            else:
                current_profit = max(current_profit, price - buy_price)
        if current_profit > 0:
            max_profit += current_profit
        return max_profit
