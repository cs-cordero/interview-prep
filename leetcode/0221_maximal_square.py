from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        M, N = len(matrix), len(matrix[0])
        histograms = [[0] * N for _ in range(M)]
        for col in range(N):
            for row in range(M):
                if matrix[row][col] == "0":
                    histograms[row][col] = 0
                    continue
                histograms[row][col] = histograms[row - 1][col] + 1 if row > 0 else 1

        largest_square = 0
        for histogram in histograms:
            i = 0
            while i < len(histogram):
                max_size = histogram[i]
                j = i
                while max_size > j - i and j < len(histogram):
                    j += 1
                    if j < len(histogram):
                        max_size = min(max_size, histogram[j])
                largest_square = max(largest_square, (j - i) ** 2)

                while i + 1 < len(histogram) and histogram[i] >= histogram[i + 1]:
                    i += 1
                i += 1
        return largest_square
