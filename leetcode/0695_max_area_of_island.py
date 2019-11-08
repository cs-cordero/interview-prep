from collections import deque
from typing import Iterable, List, Tuple


def get_adjacent_coordinates(
    base_point: Tuple[int, int], limits: Tuple[int, int]
) -> Iterable[Tuple[int, int]]:
    x, y = base_point
    lim_x, lim_y = limits
    if x - 1 >= 0:
        yield (x - 1, y)
    if y - 1 >= 0:
        yield (x, y - 1)
    if x + 1 < lim_x:
        yield (x + 1, y)
    if y + 1 < lim_y:
        yield (x, y + 1)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        limits = len(grid), len(grid[0])
        biggest_island = 0

        for row_i, row in enumerate(grid):
            for col_i, col in enumerate(row):
                if col == 0:
                    continue

                island_size = 0
                queue = deque([(row_i, col_i)])
                grid[row_i][col_i] = 0
                while queue:
                    x, y = queue.popleft()
                    island_size += 1
                    for adj_x, adj_y in get_adjacent_coordinates((x, y), limits):
                        if grid[adj_x][adj_y] == 1:
                            grid[adj_x][adj_y] = 0
                            queue.append((adj_x, adj_y))
                biggest_island = max(biggest_island, island_size)
        return biggest_island
