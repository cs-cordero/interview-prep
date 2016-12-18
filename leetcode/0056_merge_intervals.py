from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        if not intervals:
            return results

        intervals = sorted(intervals)
        lo, hi = intervals[0]
        for next_lo, next_hi in intervals[1:]:
            if next_lo <= hi:
                hi = max(hi, next_hi)
            else:
                results.append([lo, hi])
                lo, hi = next_lo, next_hi

        results.append([lo, hi])
        return results


foo = Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
assert foo == [[1, 6], [8, 10], [15, 18]]
