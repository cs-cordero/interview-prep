from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return matrix

        M = len(matrix)
        N = len(matrix[0])
        result = [[float("inf") for _ in range(N)] for _ in range(M)]

        queue = deque()
        for row in range(M):
            for col in range(N):
                if matrix[row][col] == 0:
                    queue.append((row, col, 0))
                    result[row][col] = 0

        while queue:
            row, col, steps = queue.popleft()
            if row < 0 or col < 0 or row >= M or col >= N:
                continue

            if steps > result[row][col]:
                continue

            result[row][col] = steps

            for next_row, next_col in [
                (row - 1, col),
                (row, col - 1),
                (row + 1, col),
                (row, col + 1),
            ]:
                queue.append((next_row, next_col, steps + 1))
        return result
