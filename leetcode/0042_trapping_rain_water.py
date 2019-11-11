from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        highest_index = max(range(len(height)), key=lambda x: (height[x], x))
        from_left = helper(height[: highest_index + 1])
        from_right = helper(reversed(height[highest_index:]))
        return from_left + from_right


def helper(height: List[int]) -> int:
    answer = 0
    stack = []
    lower_count = 0
    for i, elevation in enumerate(height):
        if not stack:
            stack.append(elevation)
            continue

        if elevation >= stack[-1]:
            answer += lower_count
            lower_count = 0
            stack.append(elevation)
        elif elevation < stack[-1]:
            lower_count += stack[-1] - elevation
    return answer
