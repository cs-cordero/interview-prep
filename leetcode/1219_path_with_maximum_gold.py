from typing import Iterable, List, Set, Tuple

Point = Tuple[int, int]


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        limits = len(grid), len(grid[0])

        def get_adjacent_points(base: Point) -> Iterable[Point]:
            row, col = base
            if row - 1 >= 0:
                yield (row - 1, col)
            if col - 1 >= 0:
                yield (row, col - 1)
            if row + 1 < limits[0]:
                yield (row + 1, col)
            if col + 1 < limits[1]:
                yield (row, col + 1)

        def dfs(point: Point, visited: Set[Point]) -> int:
            visited.add(point)
            row, col = point

            if grid[row][col] == 0:
                return 0

            best = float("-inf")
            for adj_point in get_adjacent_points(point):
                if adj_point in visited:
                    continue
                best = max(best, dfs(adj_point, visited.copy()) + grid[row][col])
            return best

        answer = float("-inf")
        for row_i, row in enumerate(grid):
            for col_i, _ in enumerate(row):
                result = dfs((row_i, col_i), set())
                answer = max(answer, result)
        return answer
