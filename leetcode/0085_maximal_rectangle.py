from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        cum_col_sums = [[0 for _ in range(cols)] for _ in range(rows + 1)]
        cum_col_sums[1] = [int(val) for val in matrix[0]]
        for row in range(1, rows):
            for col in range(cols):
                value = int(matrix[row][col])
                if value == 0:
                    cum_col_sums[row + 1][col] = 0
                else:
                    cum_col_sums[row + 1][col] = cum_col_sums[row][col] + value

        answer = 0
        for top in range(1, len(cum_col_sums)):
            seen_zero = [False for _ in range(cols)]
            for bottom in range(top, len(cum_col_sums)):
                current = 0
                for col, value in enumerate(cum_col_sums[bottom]):
                    if value == 0 or seen_zero[col]:
                        seen_zero[col] = True
                        current = 0
                    else:
                        current += value - cum_col_sums[top - 1][col]
                        answer = max(answer, current)
        return answer
