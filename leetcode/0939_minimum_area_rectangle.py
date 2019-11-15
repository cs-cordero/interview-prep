from collections import defaultdict
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        row_mapping = defaultdict(set)
        col_mapping = defaultdict(set)
        for point in points:
            r, c = point
            row_mapping[r].add(c)
            col_mapping[c].add(r)

        min_area = float("inf")
        for r1, cols_set in row_mapping.items():
            cols = list(cols_set)
            for i in range(len(cols) - 1):
                for j in range(i + 1, len(cols)):
                    c1 = cols[i]
                    c2 = cols[j]
                    nearest_row = min(
                        {r2 for r2 in col_mapping[c1] & col_mapping[c2] if r2 != r1},
                        key=lambda r2: abs(r2 - r1),
                        default=None,
                    )
                    if nearest_row is not None:
                        min_area = min(min_area, abs(nearest_row - r1) * abs(c2 - c1))
        return min_area if min_area != float("inf") else 0


print(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))
print(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))
