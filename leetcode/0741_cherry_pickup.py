from typing import List, Tuple

Point = Tuple[int, int]


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        memo = {}

        def helper(rowA: int, colA: int, colB: int) -> int:
            rowB = rowA + colA - colB
            key = (rowA, colA, colB)

            if any(coordinate >= N for coordinate in [rowA, colA, rowB, colB]):
                return -999999

            value_at_a = grid[rowA][colA]
            value_at_b = grid[rowB][colB]
            if value_at_a == -1 or value_at_b == -1:
                return -999999
            elif (rowA, colA) == (N - 1, N - 1):
                return grid[rowA][colA]
            elif key in memo:
                return memo[key]
            else:
                on_same_cell = (rowA, colA) == (rowB, colB)
                cherries = 0
                cherries += 1 if value_at_a == 1 else 0
                cherries += 1 if value_at_b == 1 and not on_same_cell else 0
                cherries += max(
                    helper(rowA + 1, colA, colB + 1),
                    helper(rowA, colA + 1, colB + 1),
                    helper(rowA, colA + 1, colB),
                    helper(rowA + 1, colA, colB),
                )
                memo[key] = cherries
            return memo[key]

        return max(0, helper(0, 0, 0))


grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
print(Solution().cherryPickup(grid))

grid2 = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
print(Solution().cherryPickup(grid2))

grid3 = [
    [1, -1, 1, 1, 1, 1, 1, 1, -1, 1],
    [1, 1, 1, 1, -1, -1, 1, 1, 1, 1],
    [-1, 1, 1, -1, 1, 1, 1, 1, 1, 1],
    [1, 1, -1, 1, -1, 1, 1, 1, 1, 1],
    [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [-1, -1, 1, 1, 1, -1, 1, 1, -1, 1],
    [1, 1, 1, 1, 1, 1, 1, -1, 1, 1],
    [1, 1, 1, 1, -1, 1, -1, -1, 1, 1],
    [1, -1, 1, -1, -1, 1, 1, -1, 1, -1],
    [-1, 1, -1, 1, -1, 1, 1, 1, 1, 1],
]
print(Solution().cherryPickup(grid3))

grid4 = [
    [0, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [-1, 1, 1, 1, -1],
    [0, 1, 1, 1, 0],
    [1, 0, -1, 0, 0],
]
print(Solution().cherryPickup(grid4))
