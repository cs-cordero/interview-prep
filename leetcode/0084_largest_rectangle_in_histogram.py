from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []

        for height in heights:
            lower_count = 0
            while stack and height < stack[-1][0]:
                stack_height, stack_count = stack.pop()
                lower_count += stack_count
                best = max(best, stack_height * lower_count)
            stack.append((height, lower_count + 1))

        lower_count = 0
        while stack:
            stack_height, stack_count = stack.pop()
            lower_count += stack_count
            best = max(best, stack_height * lower_count)
        return best
