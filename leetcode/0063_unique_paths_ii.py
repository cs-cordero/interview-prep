from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid) + 1)]
        for col in range(len(dp[0])):
            dp[0][col] = 0
        for row in range(len(dp)):
            dp[row][0] = 0
        dp[1][1] = 1

        for row_i, row in enumerate(dp[1:], 1):
            for col_i, _ in enumerate(dp[row_i][1:], 1):
                if obstacleGrid[row_i - 1][col_i - 1] == 1:
                    dp[row_i][col_i] = 0
                    continue

                if row_i == 1 and col_i == 1:
                    continue
                dp[row_i][col_i] = dp[row_i - 1][col_i] + dp[row_i][col_i - 1]

        for row in dp:
            print(row)
        return dp[-1][-1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(Solution().uniquePathsWithObstacles([[1]]))
