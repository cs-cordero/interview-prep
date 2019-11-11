import math
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        from_left = 0
        for seat in seats:
            if seat:
                break
            from_left += 1

        from_right = 0
        for seat in reversed(seats):
            if seat:
                break
            from_right += 1

        longest_consecutive_empty = 0
        consecutive_empty = 0
        for seat in seats:
            if seat:
                consecutive_empty = 0
            else:
                consecutive_empty += 1
                longest_consecutive_empty = max(
                    longest_consecutive_empty, consecutive_empty
                )

        return max(math.ceil(longest_consecutive_empty / 2), from_left, from_right)
