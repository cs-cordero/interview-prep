from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def place_in_correct_position(value: int) -> None:
            while nums[value - 1] not in (value, None):
                temp = nums[value - 1]
                nums[value - 1] = value
                value = temp

            if nums[value - 1] is None:
                nums[value - 1] = value

        i = 0
        while i < len(nums):
            temp = nums[i]
            nums[i] = None
            place_in_correct_position(temp)
            i += 1

        result = []
        for i, value in enumerate(nums):
            if value is None:
                result.append(i + 1)
        return result
