from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        largest = 0
        histogram = [0 for _ in range(len(matrix[0]))]
        for row in matrix:
            for col_index, value in enumerate(row):
                if value == "0":
                    histogram[col_index] = 0
                else:
                    histogram[col_index] += 1
            area = get_largest_area_of_rectangle_in_histogram(histogram)
            largest = max(area, largest)
        return largest


def get_largest_area_of_rectangle_in_histogram(hist: List[int]) -> int:
    max_area = 0
    stack = []
    for i, height in enumerate(hist):
        left_width = 0
        while stack and height < hist[stack[-1][0]]:
            j, j_left_width = stack.pop()
            left_width += j_left_width + 1
            max_area = max(max_area, hist[j] * (i - j + j_left_width))
        stack.append((i, left_width))

    i = len(hist)
    while stack:
        j, j_left_width = stack.pop()
        max_area = max(max_area, hist[j] * (i - j + j_left_width))
    return max_area
