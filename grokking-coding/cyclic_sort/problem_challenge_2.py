from typing import List


def find_first_missing_positive(nums: List[int]) -> int:
    for i in range(len(nums)):
        if nums[i] == i + 1:
            continue
        temp = nums[i]
        nums[i] = None
        while temp and temp > 0 and temp <= len(nums) and nums[temp - 1] != temp:
            next_temp = nums[temp - 1]
            nums[temp - 1] = temp
            temp = next_temp

    for i, num in enumerate(nums):
        if num is None:
            return i + 1

    return len(nums) + 1
