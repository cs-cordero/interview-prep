from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if not A or not B or len(A) != len(B):
            return -1
        if len(A) == 1:
            return 0

        first_domino, *dominos = [set(domino) for domino in zip(A, B)]
        common_values = first_domino.intersection(*dominos)
        if not common_values:
            return -1

        min_rotations = max(len(A), len(B))
        for row in [A, B]:
            for common_value in common_values:
                count = 0
                for i in range(len(row)):
                    if row[i] == common_value and (
                        (A[i] == common_value) != (B[i] == common_value)
                    ):
                        count += 1
                min_rotations = min(min_rotations, count)
        return min_rotations


print(Solution().minDominoRotations(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]))
print(Solution().minDominoRotations(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]))
