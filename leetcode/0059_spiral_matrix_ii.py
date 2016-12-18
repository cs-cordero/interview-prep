from typing import Iterable, List, Tuple


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []

        matrix = [[0] * n for _ in range(n)]
        direction_generator = turn_order()

        x, y = (0, -1)
        dx, dy = next(direction_generator)
        for i in range(1, n ** 2 + 1):
            if not (
                x + dx < n
                and y + dy < n
                and x + dx >= 0
                and y + dy >= 0
                and matrix[x + dx][y + dy] == 0
            ):
                dx, dy = next(direction_generator)
            x += dx
            y += dy
            matrix[x][y] = i
        return matrix


def turn_order() -> Iterable[Tuple[int, int]]:
    while True:
        yield (0, 1)
        yield (1, 0)
        yield (0, -1)
        yield (-1, 0)


assert Solution().spiralOrder(1) == [[1]]
assert Solution().spiralOrder(2) == [[1, 2], [4, 3]]
assert Solution().spiralOrder(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
