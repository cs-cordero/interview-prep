from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            leftmost = 0
            while stack and height < heights[stack[-1][0]]:
                j, j_left = stack.pop()
                leftmost += j_left + 1
                max_area = max(max_area, heights[j] * (i - j + j_left))
            stack.append((i, leftmost))

        i = len(heights)
        while stack:
            j, j_left = stack.pop()
            max_area = max(max_area, heights[j] * (i - j + j_left))
        return max_area


"""
[2, 1, 5, 6, 2, 3]

stack = [

best    2
current 1

popped_value 2
popped_index 0
popped_hiddn 0

rectangle_to_left 1 *

"""
