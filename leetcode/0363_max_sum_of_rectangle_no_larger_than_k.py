from bisect import bisect_left, insort
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0

        if len(matrix) > len(matrix[0]):
            # Problem explains that that the number of rows may greatly exceed
            # the number of columns.  The algorithm below operates O(N^2) where
            # N is the number of rows, so it's a huge speed-up if we transpose
            # the matrix first.
            matrix = [list(a) for a in zip(*matrix)]

        best_sub_rectangle_sum = float("-inf")
        for top_row in range(len(matrix)):
            sums_by_column = [0 for _ in range(len(matrix[0]))]
            for bottom_row in range(top_row, len(matrix)):
                for bottom_column, column_value in enumerate(matrix[bottom_row]):
                    sums_by_column[bottom_column] += column_value

                rectangles_in_order = [0]
                current_sub_rectangle_sum = 0
                for sum_value in sums_by_column:
                    current_sub_rectangle_sum += sum_value
                    if current_sub_rectangle_sum == k:
                        return k
                    else:
                        index = bisect_left(
                            rectangles_in_order, current_sub_rectangle_sum - k
                        )
                        if index < len(rectangles_in_order):
                            best_sub_rectangle_sum = max(
                                best_sub_rectangle_sum,
                                current_sub_rectangle_sum - rectangles_in_order[index],
                            )
                        insort(rectangles_in_order, current_sub_rectangle_sum)
        return best_sub_rectangle_sum


print(Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))
print(Solution().maxSumSubmatrix([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 10))
print(Solution().maxSumSubmatrix([[2, 2, -1]], 0))
print(Solution().maxSumSubmatrix([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 3))
"""
[
    [5, -4, -3, 4],
    [-3, -4, 4, 5],
    [5, 1, 5, -4]]
"""
