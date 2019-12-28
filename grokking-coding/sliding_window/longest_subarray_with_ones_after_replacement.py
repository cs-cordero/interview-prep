from typing import List


def length_of_longest_substring(arr: List[int], k: int) -> int:
    best = 0
    begin = 0
    zero_count = 0
    for end in range(len(arr)):
        if arr[end] == 0:
            zero_count += 1

        while zero_count > k:
            zero_count -= 1 if arr[begin] == 0 else 0
            begin += 1

        best = max(best, end - begin + 1)
    return best


assert length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2) == 6
assert length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3) == 9
