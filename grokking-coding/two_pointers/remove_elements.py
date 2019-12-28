from typing import List


def remove_element(arr: List[int], key: int) -> int:
    swap_point = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[i], arr[swap_point] = arr[swap_point], arr[i]
            swap_point += 1
    return swap_point


test1 = [3, 2, 3, 6, 3, 10, 9, 3]
assert remove_element(test1, 3) == 4
assert test1[:4] == [2, 6, 10, 9]


test2 = [2, 11, 2, 2, 1]
assert remove_element(test2, 2) == 2
assert test2[:2] == [11, 1]
