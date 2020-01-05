from typing import List


def can_partition_bottom_up(nums: List[int], k: int) -> bool:
    if k == 0:
        return True

    subset_sums = {0}
    for num in nums:
        next_sums = set()
        for val in subset_sums:
            value = num + val
            if value == k:
                return True
            next_sums.add(value)
        subset_sums |= next_sums
    return False


def main():
    assert can_partition_bottom_up([1, 2, 3, 7], 6) is True
    assert can_partition_bottom_up([1, 2, 7, 1, 5], 10) is True
    assert can_partition_bottom_up([1, 3, 4, 8], 6) is False


main()
