from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1 for _ in range(len(nums))]
        negative_count = 0
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = negative_count

            value = nums[i]
            if value == 0:
                negative_count = 0
            elif value < 0:
                negative_count += 1

        def helper(start: int, allow_recurse: bool = True) -> int:
            current = 1
            best = float("-inf")
            for i, num in enumerate(nums[start:], start):
                current *= num
                best = max(best, current)
                if allow_recurse and current < 0 and dp[i] % 2 == 0:
                    best = max(best, helper(i + 1, False))
                if current == 0 or (current < 0 and dp[i] == 0):
                    current = 1
            return best

        return helper(0)


print(Solution().maxProduct([2, -5, -2, -4, 3]))
