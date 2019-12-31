from typing import List


def find_corrupt_numbers(nums: List[int]) -> List[int]:
    result = []

    for i in range(len(nums)):
        if nums[i] == i + 1:
            continue
        temp = nums[i]
        nums[i] = None
        while temp and temp > 0 and temp <= len(nums):
            if temp == nums[temp - 1]:
                result.append(temp)
                break
            next_temp = nums[temp - 1]
            nums[temp - 1] = temp
            temp = next_temp

    for i, num in enumerate(nums):
        if num is None:
            result.append(i + 1)
            break

    return result
