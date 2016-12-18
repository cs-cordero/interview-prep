from collections import deque
from typing import List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for row_index, row in enumerate(grid):
            for col_index, value in enumerate(row):
                if int(value) < 1:
                    continue
                islands += 1
                mark_island(grid, (row_index, col_index))
        return islands


def mark_island(grid: List[List[str]], start: Tuple[int, int]) -> None:
    queue = deque([start])
    seen = set()
    while queue:
        row, col = queue.popleft()
        grid[row][col] = -1
        adjacent_coordinates = [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]
        for candidate_x, candidate_y in adjacent_coordinates:
            if (
                candidate_x < 0
                or candidate_x >= len(grid)
                or candidate_y < 0
                or candidate_y >= len(grid[0])
                or (candidate_x, candidate_y) in seen
                or int(grid[candidate_x][candidate_y]) < 1
            ):
                continue
            queue.append((candidate_x, candidate_y))
            seen.add((candidate_x, candidate_y))
