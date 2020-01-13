from collections import deque
from typing import Iterable, List, Tuple


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0

        memo = {}
        target = len(grid) - 1, len(grid[0]) - 1
        queue = deque([(0, 0, 0, k)])
        while queue:
            row, col, steps, remaining = queue.popleft()
            if (row, col) == target:
                return steps

            memo_key = (row, col, remaining)
            if memo_key in memo and steps >= memo[memo_key]:
                continue
            memo[memo_key] = steps

            for next_row, next_col in get_adjacent_points_in_grid(row, col, grid):
                if grid[next_row][next_col] == 1:
                    if remaining > 0:
                        queue.append((next_row, next_col, steps + 1, remaining - 1))
                else:
                    queue.append((next_row, next_col, steps + 1, remaining))
        return -1


def get_adjacent_points_in_grid(
    row: int, col: int, grid: List[List[int]]
) -> Iterable[Tuple[int, int]]:
    if row - 1 >= 0:
        yield row - 1, col
    if col - 1 >= 0:
        yield row, col - 1
    if row + 1 < len(grid):
        yield row + 1, col
    if col + 1 < len(grid[0]):
        yield row, col + 1
