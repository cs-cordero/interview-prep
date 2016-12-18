from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        current_max = 0

        while left < right:
            h_left = height[left]
            h_right = height[right]

            lower_height = h_left if h_left < h_right else h_right
            current_max = max(current_max, lower_height * (right - left))

            if h_left > h_right:
                right -= 1
            else:
                left += 1
        return current_max
