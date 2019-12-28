from typing import List


def remove_duplicates(arr: List[int]) -> int:
    swap_point = 0
    current = None
    for i in range(len(arr)):
        if arr[i] != current:
            current = arr[i]
            arr[i], arr[swap_point] = arr[swap_point], arr[i]
            swap_point += 1
        else:
            current = arr[i]
    return swap_point
