from collections import defaultdict
from typing import List


def count_subsets(nums: List[int], k: int) -> int:
    def helper(i: int, value: int) -> int:
        if value == k:
            return 1
        elif i == len(nums) or value > k:
            return 0
        return helper(i + 1, value + nums[i]) + helper(i + 1, value)

    return helper(0, 0)


def count_subsets_bottom_up(nums: List[int], k: int) -> int:
    dp = defaultdict(int)
    dp[0] = 1
    for num in nums:
        dp_snapshot = list(dp.items())
        for val, freq in dp_snapshot:
            value = num + val
            if value > k:
                continue
            dp[value] += freq
    return dp[k]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))

    print("Total number of subsets " + str(count_subsets_bottom_up([1, 1, 2, 3], 4)))
    print(
        "Total number of subsets: " + str(count_subsets_bottom_up([1, 2, 7, 1, 5], 9))
    )


main()
