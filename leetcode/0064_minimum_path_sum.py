from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        dp = [
            [float("inf") for _ in range(len(grid[0]) + 1)]
            for _ in range(len(grid) + 1)
        ]
        for row in range(len(grid) - 1, -1, -1):
            for col in range(len(grid[0]) - 1, -1, -1):
                dp_value = min(dp[row + 1][col], dp[row][col + 1])
                dp_value = 0 if dp_value == float("inf") else dp_value
                dp[row][col] = grid[row][col] + dp_value
        return dp[0][0]
