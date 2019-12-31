from typing import List


def find_missing_number(nums: List[int]) -> int:
    cyclic_sort(nums)
    for i, num in enumerate(nums):
        if num is None:
            return i
    return -1


def cyclic_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        if nums[i] == i:
            continue
        j = i
        temp = nums[j]
        nums[j] = None
        while temp is not None and temp < len(nums):
            next_temp = nums[temp]
            nums[temp] = temp
            temp = next_temp
    return nums
