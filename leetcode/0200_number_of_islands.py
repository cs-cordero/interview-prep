from collections import deque
from typing import Iterable, List, Tuple


def get_adjacent(row: int, col: int, M: int, N: int) -> Iterable[Tuple[int, int]]:
    if row - 1 >= 0:
        yield row - 1, col
    if col - 1 >= 0:
        yield row, col - 1
    if row + 1 < M:
        yield row + 1, col
    if col + 1 < N:
        yield row, col + 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        islands = 0
        if not grid or not grid[0]:
            return islands

        M, N = len(grid), len(grid[0])
        for row_i, row in enumerate(grid):
            for col_i, value in enumerate(row):
                if value == "1":
                    islands += 1
                    queue.append((row_i, col_i))
                    grid[row_i][col_i] = "0"
                while queue:
                    current_row, current_col = queue.popleft()
                    for nrow, ncol in get_adjacent(current_row, current_col, M, N):
                        if grid[nrow][ncol] == "1":
                            grid[nrow][ncol] = "0"
                            queue.append((nrow, ncol))
        return islands
