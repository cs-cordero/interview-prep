from typing import Iterable, List, Tuple

Point = Tuple[int, int]


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        limits = len(matrix), len(matrix[0])

        def get_adjacent_points(
            point: Point, limits: Tuple[int, int]
        ) -> Iterable[Point]:
            x, y = point
            current_value = matrix[x][y]
            if x - 1 >= 0 and matrix[x - 1][y] > current_value:
                yield x - 1, y
            if y - 1 >= 0 and matrix[x][y - 1] > current_value:
                yield x, y - 1
            if x + 1 < limits[0] and matrix[x + 1][y] > current_value:
                yield x + 1, y
            if y + 1 < limits[1] and matrix[x][y + 1] > current_value:
                yield x, y + 1

        def helper(point: Point) -> int:
            r, c = point
            if dp[r][c]:
                return dp[r][c]

            results_from_adjacent = [
                helper(adjacent) for adjacent in get_adjacent_points(point, limits)
            ]
            dp[r][c] = max([0, *results_from_adjacent]) + 1
            return dp[r][c]

        best = float("-inf")
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                best = max(best, helper((r, c)))
        return best


print(Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
