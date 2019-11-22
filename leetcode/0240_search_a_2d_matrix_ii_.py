from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(
            top_row: int, top_col: int, bottom_row: int, bottom_col: int
        ) -> bool:
            row_out_of_bounds = any(
                row < 0 or row >= len(matrix) for row in (top_row, bottom_row)
            )
            col_out_of_bounds = any(
                col < 0 or col >= len(matrix[0]) for col in (top_col, bottom_col)
            )
            row_switched = top_row > bottom_row
            col_switched = top_col > bottom_col
            if row_out_of_bounds or col_out_of_bounds or row_switched or col_switched:
                return False

            mid_row = (top_row + bottom_row) // 2
            mid_col = (top_col + bottom_col) // 2

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                return (
                    helper(top_row, top_col, mid_row - 1, mid_col - 1)
                    or helper(top_row, mid_col, mid_row - 1, bottom_col)
                    or helper(mid_row, top_col, bottom_row, mid_col - 1)
                )
            else:
                return (
                    helper(mid_row + 1, mid_col + 1, bottom_row, bottom_col)
                    or helper(mid_row + 1, top_col, bottom_row, mid_col)
                    or helper(top_row, mid_col + 1, mid_row, bottom_col)
                )

        if not matrix or not matrix[0]:
            return False
        return helper(0, 0, len(matrix) - 1, len(matrix[0]) - 1)
