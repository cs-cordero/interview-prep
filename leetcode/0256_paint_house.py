from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        dp = costs[0][:]

        for house_number, color_costs in enumerate(costs[1:], 1):
            next_color_costs = [0, 0, 0]
            for color_index, color_cost in enumerate(color_costs):
                min_cost_prev = min(
                    dp[next_color]
                    for next_color in range(3)
                    if next_color != color_index
                )
                next_color_costs[color_index] = min_cost_prev + color_cost
            dp = next_color_costs
        return min(dp)


print(Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
