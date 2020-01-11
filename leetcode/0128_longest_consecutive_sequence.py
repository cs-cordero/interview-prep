from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        seen = set()
        best = 0

        for num in nums:
            if num in seen:
                continue

            left = num
            while left - 1 in all_nums:
                seen.add(left - 1)
                left -= 1

            right = num
            while right + 1 in all_nums:
                seen.add(right + 1)
                right += 1

            seen.add(num)
            best = max(best, right - left + 1)
        return best
