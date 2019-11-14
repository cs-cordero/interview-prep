from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        result = []
        sorted_intervals = sorted(intervals)
        low, high = sorted_intervals[0]
        for interval_low, interval_high in sorted_intervals[1:]:
            if (
                (interval_low <= low and interval_high >= low and interval_high <= high)
                or (
                    interval_low >= low
                    and interval_low <= high
                    and interval_high >= high
                )
                or (interval_low <= low and interval_high >= high)
                or (interval_low >= low and interval_high <= high)
            ):
                high = max(high, interval_high)
                low = min(low, interval_low)
            else:
                result.append([low, high])
                low = interval_low
                high = interval_high
        result.append([low, high])
        return result
