from typing import List


def search_bitonic_array(arr: List[int], key: int) -> int:
    max_index = binary_search_for_max_index(arr)
    return max(
        binary_search_exact(arr, key, 0, max_index),
        binary_search_exact(arr, key, max_index, len(arr) - 1, True),
    )


def binary_search_exact(
    arr: List[int], key: int, left: int, right: int, desc: bool = False
) -> int:
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid

        if desc is False:
            if arr[mid] > key:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
    return -1


def binary_search_for_max_index(arr: List[int]) -> int:
    left = 1
    right = len(arr) - 2
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid - 1]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
