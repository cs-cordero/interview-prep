from collections import deque
from typing import List, Set, Tuple

Point = Tuple[int, int]


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        transform_grid(grid)

        building_locations = get_building_locations(grid)
        for building_location in building_locations:
            reached = bfs(grid, building_location)
            if len(reached) != len(building_locations):
                return -1

        highest_value = float("-inf")
        for row_i, row in enumerate(grid):
            for col_i, (value, reach) in enumerate(row):
                if value > 0 or reach != len(building_locations):
                    continue
                highest_value = max(highest_value, value)
        return abs(highest_value) if highest_value != float("-inf") else -1


def transform_grid(grid: List[List[int]]) -> Set[Point]:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            value = grid[row][col]
            grid[row][col] = (value, 0)


def get_building_locations(grid: List[List[int]]) -> Set[Point]:
    result = set()
    for row_i, row in enumerate(grid):
        for col_i, (value, _) in enumerate(row):
            if value == 1:
                result.add((row_i, col_i))
    return result


def bfs(grid: List[List[int]], start: Point) -> Set[Point]:
    queue = deque([(*start, 0)])
    visited = {start}
    buildings_seen = {start}
    while queue:
        row, col, steps = queue.popleft()
        for drow, dcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            next_row, next_col = row + drow, col + dcol
            if next_row < 0 or next_row >= len(grid):
                continue
            elif next_col < 0 or next_col >= len(grid[0]):
                continue
            elif (next_row, next_col) in visited:
                continue

            next_point = (next_row, next_col)
            visited.add(next_point)
            current_steps, reach = grid[next_row][next_col]
            if current_steps == 2:
                continue
            elif current_steps == 1:
                buildings_seen.add(next_point)
                continue
            current_steps -= steps + 1
            reach += 1
            grid[next_row][next_col] = (current_steps, reach)
            queue.append((next_row, next_col, steps + 1))
    return buildings_seen


print(Solution().shortestDistance([[1, 2, 0]]))

print(
    Solution().shortestDistance(
        [
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 0],
        ]
    )
)
