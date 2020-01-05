from typing import List


def solve_knapsack(profits: List[int], weights: List[int], capacity: int) -> int:
    def helper(index: int, current_capacity: int, current_profit: int) -> int:
        if current_capacity < 0:
            return 0
        elif index == len(profits):
            return current_profit

        weight = weights[index]
        profit = profits[index]
        return max(
            current_profit,
            helper(index + 1, current_capacity - weight, current_profit + profit),
            helper(index + 1, current_capacity, current_profit),
        )

    return helper(0, capacity, 0)


def solve_knapsack_top_down(
    profits: List[int], weights: List[int], capacity: int
) -> int:
    memo = {}

    def helper(index: int, current_capacity: int, current_profit: int) -> int:
        key = (index, current_capacity)
        if key not in memo:
            if current_capacity < 0:
                memo[key] = 0
            elif index == len(profits):
                memo[key] = current_profit
            else:
                weight = weights[index]
                profit = profits[index]
                memo[key] = max(
                    current_profit,
                    helper(
                        index + 1, current_capacity - weight, current_profit + profit
                    ),
                    helper(index + 1, current_capacity, current_profit),
                )
        return memo[key]

    return helper(0, capacity, 0)


def solve_knapsack_bottom_up(
    profits: List[int], weights: List[int], capacity: int
) -> int:
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits) + 1)]
    for i, (profit, weight) in enumerate(zip(profits, weights), 1):
        for j in range(1, capacity + 1):
            profit_by_taking_item = 0 if j < weight else dp[i - 1][j - weight] + profit
            profit_by_skipping_item = dp[i][j - 1]
            dp[i][j] = max(dp[i - 1][j], profit_by_taking_item, profit_by_skipping_item)
    return dp[-1][-1]


def solve_knapsack_bottom_up_space_optimized(
    profits: List[int], weights: List[int], capacity: int
) -> int:
    dp = [[0 for _ in range(capacity + 1)] for _ in range(2)]
    for i, (profit, weight) in enumerate(zip(profits, weights), 1):
        for j in range(1, capacity + 1):
            profit_by_taking_item = (
                0 if j < weight else dp[(i - 1) % 2][j - weight] + profit
            )
            profit_by_skipping_item = dp[i % 2][j - 1]
            dp[i % 2][j] = max(
                dp[(i - 1) % 2][j], profit_by_taking_item, profit_by_skipping_item
            )
    return dp[i % 2][-1]


def main():
    assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
    assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17

    assert solve_knapsack_top_down([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
    assert solve_knapsack_top_down([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17

    assert solve_knapsack_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
    assert solve_knapsack_bottom_up([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17

    assert (
        solve_knapsack_bottom_up_space_optimized([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
    )
    assert (
        solve_knapsack_bottom_up_space_optimized([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17
    )


main()
