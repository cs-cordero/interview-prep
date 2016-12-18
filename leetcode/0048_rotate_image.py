from typing import Iterable, List, Tuple


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        dimension = len(matrix)
        for row in range(dimension // 2 + (dimension % 2 != 0)):
            for col in range(row, dimension - row - 1):
                temp = matrix[row][col]
                for corner_x, corner_y in all_corners(row, col, dimension):
                    matrix[corner_x][corner_y], temp = temp, matrix[corner_x][corner_y]


def all_corners(row: int, col: int, dimension: int) -> Iterable[Tuple[int, int]]:
    yield col, dimension - row - 1
    yield dimension - row - 1, dimension - col - 1
    yield dimension - col - 1, row
    yield row, col


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(matrix2)
assert matrix2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
