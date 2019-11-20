from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        seen = set()
        best = 0
        current = 0
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            current = 1

            # Scan forward
            other_num = num + 1
            while other_num in all_nums:
                seen.add(other_num)
                current += 1
                other_num += 1

            # Scan backward
            other_num = num - 1
            while other_num in all_nums:
                seen.add(other_num)
                current += 1
                other_num -= 1

            best = max(current, best)

        return best
