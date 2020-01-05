from typing import List


def solve_rod_cutting(lengths: List[int], prices: List[int], n: int) -> int:
    def helper(profit: int, length: int) -> int:
        if length < 0:
            return 0

        best = profit
        for size, price in zip(lengths, prices):
            if size > length:
                continue
            best = max(best, helper(profit + price, length - size))
        return best

    return helper(0, n)


def solve_rod_cutting_alternate(lengths: List[int], prices: List[int], n: int) -> int:
    dp = [0 for _ in range(n + 1)]
    for i in range(1, len(dp)):
        for length, price in zip(lengths, prices):
            if length > i:
                continue
            dp[i] = max(dp[i], price + dp[i - length])
    return dp[-1]


def main():
    print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))
    print(solve_rod_cutting_alternate([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()
