from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        pacific = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        atlantic = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for m in range(len(matrix)):
            pacific[m][0] = True
            atlantic[m][-1] = True
        for n in range(len(matrix[0])):
            pacific[0][n] = True
            atlantic[-1][n] = True

        find_flow(matrix, pacific)
        find_flow(matrix, atlantic)

        result = []
        for row_i, row in enumerate(pacific):
            for col_i, value in enumerate(row):
                if value and atlantic[row_i][col_i]:
                    result.append((row_i, col_i))
        return result


def find_flow(matrix: List[List[int]], dp_matrix: List[List[int]]) -> None:
    queue = deque(
        [
            (row_i, col_i)
            for row_i, row in enumerate(dp_matrix)
            for col_i, value in enumerate(row)
            if value
        ]
    )
    deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while queue:
        row, col = queue.popleft()
        value = matrix[row][col]
        neighbors = [(row + drow, col + dcol) for drow, dcol in deltas]
        for nrow, ncol in neighbors:
            if (
                nrow < 0
                or ncol < 0
                or nrow >= len(matrix)
                or ncol >= len(matrix[nrow])
                or dp_matrix[nrow][ncol]
            ):
                continue
            if value <= matrix[nrow][ncol]:
                dp_matrix[nrow][ncol] = True
                queue.append((nrow, ncol))


matrix = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(Solution().pacificAtlantic(matrix))

matrix2 = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(Solution().pacificAtlantic(matrix2))
