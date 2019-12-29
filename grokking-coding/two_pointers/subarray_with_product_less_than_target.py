from typing import List


def find_subarrays(arr: List[int], target: int) -> List[List[int]]:
    result = []
    for start in range(len(arr)):
        current = 1
        for end in range(start, len(arr)):
            current *= arr[end]
            if current < target:
                result.append(arr[start : end + 1])
            else:
                break
    return result
