from typing import List


def cyclic_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        if nums[i] == i + 1:
            continue
        j = i
        temp = nums[j]
        nums[j] = None
        while temp is not None:
            next_temp = nums[temp - 1]
            nums[temp - 1] = temp
            temp = next_temp
    return nums
