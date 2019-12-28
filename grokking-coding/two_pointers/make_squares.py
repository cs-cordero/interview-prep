from typing import List


def make_squares(arr: List[int]) -> List[int]:
    squares = []
    if not arr:
        return squares

    left = len(arr) // 2
    right = left + 1
    while left >= 0 or right < len(arr):
        if left >= 0 and (right == len(arr) or abs(arr[left]) < abs(arr[right])):
            squares.append(arr[left] ** 2)
            left -= 1
        else:
            squares.append(arr[right] ** 2)
            right += 1
    return squares
