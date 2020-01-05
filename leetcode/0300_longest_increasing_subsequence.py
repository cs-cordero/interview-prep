from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [-1 for _ in range(len(nums))]

        def helper(i: int) -> int:
            if dp[i] == -1:
                current = nums[i]
                longest = 0
                for j in range(i + 1, len(nums)):
                    candidate = nums[j]
                    if current >= candidate:
                        continue
                    longest = max(longest, helper(j))
                dp[i] = longest + 1
            return dp[i]

        for i in range(len(nums) - 1, -1, -1):
            helper(i)
        return max(dp)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
