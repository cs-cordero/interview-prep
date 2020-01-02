from typing import List


def count_rotations(arr: List[int]) -> int:
    if not arr or len(arr) == 1 or arr[0] < arr[-1]:
        return 0

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            return mid

        left_is_sorted = arr[left] <= arr[mid]
        if left_is_sorted:
            left = mid + 1
        else:
            right = mid - 1
    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
