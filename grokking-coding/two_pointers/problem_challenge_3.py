from typing import List


def shortest_window_sort(arr: List[int]) -> int:
    begin = None
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            begin = i - 1
            break

    if begin is None:
        return 0

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < arr[i - 1]:
            end = i
            break

    min_in_window = min(arr[begin : end + 1])
    max_in_window = max(arr[begin : end + 1])

    for leftmost in range(begin + 1):
        if arr[leftmost] > min_in_window:
            begin = leftmost
            break

    for rightmost in range(len(arr) - 1, end - 1, -1):
        if arr[rightmost] < max_in_window:
            end = rightmost
            break

    return end - begin + 1


print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(shortest_window_sort([1, 2, 3]))
print(shortest_window_sort([3, 2, 1]))
print(shortest_window_sort([]))
print(shortest_window_sort([1]))
