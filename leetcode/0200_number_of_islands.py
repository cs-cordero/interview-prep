from collections import deque
from typing import Iterable, List, Tuple

Point = Tuple[int, int]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid or not grid[0]:
            return islands

        limits = len(grid), len(grid[0])
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                if value == "0":
                    continue
                queue = deque([(row_index, col_index)])
                while queue:
                    x1, y1 = queue.popleft()
                    grid[x1][y1] = "0"
                    for x2, y2 in get_adjacent_points((x1, y1), limits):
                        if grid[x2][y2] == "1":
                            grid[x2][y2] = "0"
                            queue.append((x2, y2))
                islands += 1

        return islands


def get_adjacent_points(point: Point, limits: Tuple[int, int]) -> Iterable[Point]:
    x, y = point
    if x - 1 >= 0:
        yield x - 1, y
    if y - 1 >= 0:
        yield x, y - 1
    if x + 1 < limits[0]:
        yield x + 1, y
    if y + 1 < limits[1]:
        yield x, y + 1
