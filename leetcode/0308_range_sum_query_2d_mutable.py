from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix
        self.prefix_sums = []
        for row in matrix:
            prefix_row = row[:]
            for i in range(1, len(prefix_row)):
                prefix_row[i] = prefix_row[i] + prefix_row[i - 1]
            self.prefix_sums.append(prefix_row)

    def update(self, row: int, col: int, val: int) -> None:
        original_value = self.matrix[row][col]
        differential = val - original_value
        self.matrix[row][col] = val
        for i in range(col, len(self.prefix_sums[row])):
            self.prefix_sums[row][i] += differential

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
            prefix_row = self.prefix_sums[row]
            total += prefix_row[col2]
            total -= prefix_row[col1 - 1] if col1 > 0 else 0
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
