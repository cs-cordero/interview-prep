from typing import Iterable, List, Tuple


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        direction_generator = turn_order()
        element_count = len(matrix) * len(matrix[0])
        x, y = (0, -1)

        spiral = []
        while len(spiral) < element_count:
            dx, dy = next(direction_generator)
            while (
                x + dx < len(matrix)
                and y + dy < len(matrix[0])
                and x + dx >= 0
                and y + dy >= 0
                and matrix[x + dx][y + dy] is not None
            ):
                x += dx
                y += dy
                spiral.append(matrix[x][y])
                matrix[x][y] = None
        return spiral


def turn_order() -> Iterable[Tuple[int, int]]:
    while True:
        yield (0, 1)
        yield (1, 0)
        yield (0, -1)
        yield (-1, 0)


assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    1,
    2,
    3,
    6,
    9,
    8,
    7,
    4,
    5,
]
assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
    1,
    2,
    3,
    4,
    8,
    12,
    11,
    10,
    9,
    5,
    6,
    7,
]
assert Solution().spiralOrder([]) == []
