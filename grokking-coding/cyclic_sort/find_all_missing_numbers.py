from typing import List


def find_missing_numbers(nums: List[int]) -> List[int]:
    missing_numbers = []
    cyclic_sort(nums)
    for i, num in enumerate(nums):
        if num is None:
            missing_numbers.append(i + 1)
    return missing_numbers


def cyclic_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        if nums[i] == i + 1:
            continue
        j = i
        temp = nums[j]
        nums[j] = None
        while temp is not None and temp > 0 and temp <= len(nums):
            if nums[temp - 1] == temp:
                break
            next_temp = nums[temp - 1]
            nums[temp - 1] = temp
            temp = next_temp
    return nums
