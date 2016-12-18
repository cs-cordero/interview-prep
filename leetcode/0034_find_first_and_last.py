from typing import List, Tuple


def solution(arr: List[int], num: int) -> Tuple[int, int]:
    first = bisect(arr, num, True)
    last = bisect(arr, num, False)
    return (first, last)


def bisect(arr: List[int], target: int, first: bool) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > target:
            right = mid - 1
            continue
        elif arr[mid] < target:
            left = mid + 1
            continue

        if first:
            if mid == 0 or arr[mid - 1] < arr[mid]:
                return mid
            right = mid - 1

        else:
            if mid == len(arr) - 1 or arr[mid + 1] > arr[mid]:
                return mid
            left = mid + 1
    return -1


print(solution([5, 7, 7, 8, 8, 10], 8))
print(solution([5, 7, 7, 8, 8, 10], 6))
