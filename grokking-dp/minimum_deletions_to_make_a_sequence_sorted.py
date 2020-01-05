from typing import List


def find_minimum_deletions(nums: List[int]) -> int:
    return len(nums) - lis(nums)


def lis(nums: List[int]) -> int:
    dp = [1 for _ in range(len(nums))]
    longest = 1
    for i, value in enumerate(nums):
        for j in range(i):
            prev_value = nums[j]
            if prev_value < value:
                dp[i] = dp[j] + 1
                longest = max(longest, dp[i])
    return longest


def main():
    print(find_minimum_deletions([4, 2, 3, 6, 10, 1, 12]))
    print(find_minimum_deletions([-4, 10, 3, 7, 15]))
    print(find_minimum_deletions([3, 2, 1, 0]))


main()
