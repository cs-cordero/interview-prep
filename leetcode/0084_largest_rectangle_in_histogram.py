from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        def count_rectangular_candidates(_heights):
            stack = []
            counts = []
            for i, height in enumerate(_heights):
                count = 0
                while stack:
                    stack_val, stack_cnt = stack[-1]
                    if height <= stack_val:
                        stack.pop()
                        count += 1 + stack_cnt
                    else:
                        break
                stack.append((height, count))
                counts.append(count)
            return counts

        from_left = count_rectangular_candidates(heights)
        from_right = count_rectangular_candidates(reversed(heights))
        return max(
            height * (a + b + 1)
            for height, a, b in zip(heights, from_left, reversed(from_right))
        )


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
