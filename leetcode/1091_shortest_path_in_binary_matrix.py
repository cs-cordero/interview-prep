from collections import deque
from typing import Iterable, List, Tuple


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        queue = deque()
        visited = set()

        if grid[0][0] == 0:
            queue.append((0, 0, 1))
            visited.add((0, 0))

        while queue:
            row, col, steps = queue.popleft()
            if row == (len(grid) - 1) and col == (len(grid[0]) - 1):
                return steps
            for next_row, next_col in get_neighbors(row, col, len(grid), len(grid[0])):
                if (next_row, next_col) in visited:
                    continue
                visited.add((next_row, next_col))

                if grid[next_row][next_col] == 1:
                    continue
                queue.append((next_row, next_col, steps + 1))
        return -1


def get_neighbors(
    row: int, col: int, lim_row: int, lim_col: int
) -> Iterable[Tuple[int, int]]:
    for delta_row, delta_col in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]:
        next_row, next_col = row + delta_row, col + delta_col
        if next_row < 0 or next_col < 0 or next_row >= lim_row or next_col >= lim_col:
            continue
        yield next_row, next_col
