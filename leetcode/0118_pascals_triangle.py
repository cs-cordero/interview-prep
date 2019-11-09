from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        elif numRows == 1:
            return [[1]]

        result = []
        result.extend(self.generate(numRows - 1))

        previous_row = result[-1]
        row = []
        for col in range(numRows):
            if col == 0 or col == numRows - 1:
                row.append(1)
                continue
            row.append(previous_row[col - 1] + previous_row[col])
        result.append(row)
        return result
