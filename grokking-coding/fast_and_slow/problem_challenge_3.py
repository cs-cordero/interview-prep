from typing import List


def circular_array_loop_exists(arr: List[int]) -> bool:
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow = i
        fast = i
        while True:
            slow = find_next_index(arr, is_forward, slow)
            fast = find_next_index(arr, is_forward, fast)
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow == fast and slow != -1:
            return True
    return False


def find_next_index(arr: List[int], is_forward: bool, index: int) -> int:
    direction = arr[index] >= 0
    if direction != is_forward:
        return -1

    next_index = (index + arr[index]) % len(index)
    if next_index == index:
        return -1

    return next_index


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
