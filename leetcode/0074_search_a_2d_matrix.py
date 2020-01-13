from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        def helper(lo_row: int, hi_row: int, lo_col: int, hi_col: int) -> bool:
            if lo_row == hi_row and lo_col == hi_col:
                return matrix[lo_row][lo_col] == target
            elif lo_row > hi_row or lo_col > hi_col:
                return False

            mid_row = (lo_row + hi_row) // 2
            mid_col = (lo_col + hi_col) // 2
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                below = helper(mid_row + 1, hi_row, lo_col, hi_col)
                right = helper(lo_row, mid_row, mid_col + 1, hi_col)
                return below or right
            else:
                above = helper(lo_row, mid_row - 1, lo_col, hi_col)
                left = helper(mid_row, hi_row, lo_col, mid_col - 1)
                return above or left

        return helper(0, len(matrix) - 1, 0, len(matrix[0]) - 1)
