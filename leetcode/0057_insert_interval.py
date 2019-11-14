from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        low, high = newInterval
        inserted = False
        for interval_low, interval_high in intervals:
            if not inserted and low < interval_low and high < interval_low:
                result.append([low, high])
                inserted = True

            if inserted or low > interval_high or high < interval_low:
                result.append([interval_low, interval_high])
                continue

            low = min(low, interval_low)
            high = max(high, interval_high)

        if not inserted:
            result.append([low, high])

        return result
