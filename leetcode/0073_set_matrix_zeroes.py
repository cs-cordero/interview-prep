from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        M = len(matrix)
        N = len(matrix[0])
        rows = set()
        cols = set()
        for row in range(M):
            for col in range(N):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)

        for row in rows:
            for col in range(N):
                matrix[row][col] = 0

        for col in cols:
            for row in range(M):
                matrix[row][col] = 0
