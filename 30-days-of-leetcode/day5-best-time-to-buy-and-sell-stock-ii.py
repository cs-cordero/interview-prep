from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Say you have an array for which the ith element is the price of a
        # given stock on day i.
        #
        # Design an algorithm to find the maximum profit. You may complete as
        # many transactions as you like (i.e., buy one and sell one share of
        # the stock multiple times).
        profit = 0
        if not prices:
            return profit

        buy = prices[0]
        for i, price in enumerate(prices[1:], 1):
            if price < prices[i - 1]:
                profit += prices[i - 1] - buy
                buy = price
