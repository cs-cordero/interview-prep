from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums) for _ in range(len(nums))]
        dp[0] = 0

        for jumpman in range(len(dp)):
            current_jump_count = dp[jumpman]
            possible_jump_count = nums[jumpman]
            end_jump = min(len(dp) - 1, jumpman + possible_jump_count)
            for next_jump in range(end_jump, jumpman, -1):
                if dp[next_jump] <= current_jump_count + 1:
                    break

                dp[next_jump] = current_jump_count + 1
        return dp[-1]
