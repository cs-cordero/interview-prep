from typing import List


def find_MSIS(nums: List[int]) -> int:
    dp = [None for _ in range(len(nums))]
    global_best = 0
    for i in range(len(nums) - 1, -1, -1):
        local_best = 0
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                local_best = max(local_best, dp[j])
        dp[i] = local_best + nums[i]
        global_best = max(global_best, dp[i])
    return global_best


def main():
    print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS([-4, 10, 3, 7, 15]))


main()
