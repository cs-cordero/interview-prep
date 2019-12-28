from typing import List


def triplet_with_smaller_sum(arr: List[int], target: int) -> int:
    count = 0
    arr.sort()
    for a in range(len(arr) - 2):
        b = a + 1
        c = len(arr) - 1
        local_target = target - arr[a]
        while b < c:
            current_sum = arr[b] + arr[c]
            if current_sum >= local_target:
                c -= 1
            else:
                count += c - b
                b += 1
    return count
