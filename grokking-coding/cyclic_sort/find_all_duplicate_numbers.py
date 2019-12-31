from typing import List


def find_all_duplicates(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        if nums[i] == i + 1:
            continue
        j = i
        temp = nums[j]
        nums[j] = None
        while temp is not None and temp > 0 and temp <= len(nums):
            if nums[temp - 1] == temp:
                result.append(temp)
                break
            next_temp = nums[temp - 1]
            nums[temp - 1] = temp
            temp = next_temp
    return result
