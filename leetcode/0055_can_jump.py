from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        current = 0

        while current <= furthest:
            if furthest >= len(nums) - 1:
                return True

            furthest = max(furthest, current + nums[current])
            current += 1

        return False


assert Solution().canJump([0]) is True
assert Solution().canJump([2, 3, 1, 1, 4]) is True
assert Solution().canJump([3, 2, 1, 0, 4]) is False
