from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []

        if not nums:
            result.append(generate_range_representation(lower, upper))
            return result

        if nums[0] > lower:
            result.append(generate_range_representation(lower, nums[0] - 1))

        for i, num in enumerate(nums[1:], 1):
            if num - nums[i - 1] > 1:
                result.append(generate_range_representation(nums[i - 1] + 1, num - 1))

        if nums[-1] < upper:
            result.append(generate_range_representation(nums[-1] + 1, upper))

        return result


def generate_range_representation(lower: int, upper: int) -> str:
    return str(lower) if lower == upper else f"{lower}->{upper}"
