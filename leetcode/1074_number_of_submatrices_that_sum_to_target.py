from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        matches = 0
        if not matrix or not matrix[0]:
            return matches

        cum_matrix = generate_cum_matrix(matrix)
        for slow in range(len(cum_matrix)):
            for fast in range(slow + 1, len(cum_matrix)):
                row = [
                    cum_matrix[fast][i] - cum_matrix[slow][i]
                    for i in range(len(cum_matrix[fast]))
                ]
                result = count_target_match(row, target)
                matches += result
        return matches


def generate_cum_matrix(matrix: List[List[int]]) -> List[List[int]]:
    cum_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix) + 1)]
    for row_i, row in enumerate(matrix, 1):
        for col_i, value in enumerate(row):
            cum_matrix[row_i][col_i] = cum_matrix[row_i - 1][col_i] + value
    return cum_matrix


def count_target_match(row: List[int], target: int) -> int:
    result = 0
    if not row:
        return result

    cum_row = [0 for _ in range(len(row))]
    cum_row[0] = row[0]
    for i in range(1, len(row)):
        cum_row[i] = row[i] + cum_row[i - 1]

    mapping = defaultdict(int)
    mapping[0] = 1

    for value in cum_row:
        k = value - target
        if k in mapping:
            result += mapping[k]
        mapping[value] += 1
    return result


# print(count_target_match([0, 1, 0], 0))
print(Solution().numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
print(Solution().numSubmatrixSumTarget([[1, -1], [-1, 1]], 0))
