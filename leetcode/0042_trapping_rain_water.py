from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        highest = 0
        highest_i = 0
        units_of_water = 0
        current_units_of_water = 0
        for i, height in enumerate(heights):
            if height >= highest:
                units_of_water += current_units_of_water
                current_units_of_water = 0
                highest_i = i
                highest = max(height, highest)
            else:
                current_units_of_water += highest - height

        highest = 0
        current_units_of_water = 0
        for j in range(len(heights) - 1, highest_i - 1, -1):
            height = heights[j]
            if height >= highest:
                units_of_water += current_units_of_water
                current_units_of_water = 0
                highest_i = i
                highest = max(height, highest)
            else:
                current_units_of_water += highest - height

        return units_of_water
