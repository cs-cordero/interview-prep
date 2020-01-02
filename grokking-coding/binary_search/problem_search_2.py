from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return search_rotated_array(nums, target)


def search_rotated_array(arr: List[int], key: int) -> int:
    if not arr:
        return -1

    rotation_point = binary_search_for_max_index(arr)
    print(rotation_point)
    if key <= arr[-1]:
        return binary_search_exact(arr, key, rotation_point, len(arr) - 1)
    else:
        return binary_search_exact(arr, key, 0, rotation_point)


def binary_search_exact(
    arr: List[int], key: int, left: int, right: int, desc: bool = False
) -> int:
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid

        if desc is False:
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] > key:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def binary_search_for_max_index(arr: List[int]) -> int:
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1
    leftmost = arr[left]
    while left <= right:
        mid = (left + right) // 2
        if mid == len(arr) - 1:
            if arr[mid] >= leftmost:
                return 0
            right = mid - 1

        elif arr[mid] < arr[mid + 1]:
            if arr[mid] >= leftmost:
                left = mid + 1
            else:
                right = mid - 1

        else:
            return mid + 1

    return -1
