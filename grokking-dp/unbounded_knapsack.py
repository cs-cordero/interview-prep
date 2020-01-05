from typing import List


def solve_knapsack(profits: List[int], weights: List[int], capacity: int):
    def helper(cap: int, current: int) -> int:
        if cap < 0:
            return 0
        elif cap == 0:
            return current

        best = current
        for weight, profit in zip(weights, profits):
            best = max(best, helper(cap - weight, current + profit))
        return best

    return helper(capacity, 0)


def solve_knapsack_top_down(profits: List[int], weights: List[int], capacity: int):
    memo = {}

    def helper(cap: int, current: int) -> int:
        key = (cap, current)
        if key not in memo:
            if cap < 0:
                memo[key] = 0
            elif cap == 0:
                memo[key] = current
            else:
                best = current
                for weight, profit in zip(weights, profits):
                    best = max(best, helper(cap - weight, current + profit))
                memo[key] = best

        return memo[key]

    return helper(capacity, 0)


def main():
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))

    print(solve_knapsack_top_down([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_knapsack_top_down([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
