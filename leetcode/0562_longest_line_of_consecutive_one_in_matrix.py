from dataclasses import dataclass
from typing import List


@dataclass
class DPNode:
    horizontal: int = 0
    vertical: int = 0
    diagonal: int = 0
    antidiagonal: int = 0

    @property
    def max(self) -> int:
        return max(self.horizontal, self.vertical, self.diagonal, self.antidiagonal)


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        best = 0
        if not M or not M[0]:
            return best

        dp = [[DPNode() for _ in range(len(M[0]) + 2)] for _ in range(len(M) + 1)]
        for row_i, row in enumerate(M, 1):
            for col_i, value in enumerate(row, 1):
                if value == 0:
                    continue
                node = dp[row_i][col_i]
                node.horizontal = dp[row_i][col_i - 1].horizontal + 1
                node.vertical = dp[row_i - 1][col_i].vertical + 1
                node.diagonal = dp[row_i - 1][col_i - 1].diagonal + 1
                node.antidiagonal = dp[row_i - 1][col_i + 1].antidiagonal + 1
                best = max(best, node.max)
        return best
