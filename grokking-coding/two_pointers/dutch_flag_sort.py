from typing import List


def dutch_flag_sort(arr: List[int]) -> None:
    swap_point_zero = 0
    swap_point_two = len(arr) - 1
    i = 0
    while i <= swap_point_two:
        if swap_point_zero < i and arr[i] == 0:
            arr[i], arr[swap_point_zero] = arr[swap_point_zero], arr[i]
            swap_point_zero += 1
        elif i < swap_point_two and arr[i] == 2:
            arr[i], arr[swap_point_two] = arr[swap_point_two], arr[i]
            swap_point_two -= 1
        else:
            i += 1


test1 = [1, 0, 2, 1, 0]
dutch_flag_sort(test1)
assert test1 == [0, 0, 1, 1, 2]

test2 = [2, 2, 0, 1, 2, 0]
dutch_flag_sort(test2)
assert test2 == [0, 0, 1, 2, 2, 2]
