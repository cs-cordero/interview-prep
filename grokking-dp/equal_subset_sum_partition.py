from typing import List


def can_partition(nums: List[int]) -> bool:
    # Time: (O(2^N))
    # Space: (O(N))
    def helper(i: int, difference: int) -> bool:
        if i == len(nums):
            return difference == 0
        return helper(i + 1, difference + nums[i]) or helper(
            i + 1, difference - nums[i]
        )

    return helper(0, 0)


def can_partition_top_down(nums: List[int]) -> bool:
    # Time: (O(S)), where S is the sum of the positive values in nums.
    # Space: (O(S))
    memo = {}

    def helper(i: int, difference: int) -> bool:
        key = (i, difference)
        if key not in memo:
            if i == len(nums):
                memo[key] = difference == 0
            else:
                memo[key] = helper(i + 1, difference + nums[i]) or helper(
                    i + 1, difference - nums[i]
                )
        return memo[key]

    return helper(0, 0)


def can_partition_bottom_up(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    subset_sums = {0}
    for num in nums:
        next_sums = set()
        for subset_sum in subset_sums:
            value = num + subset_sum
            if value < target:
                next_sums.add(value)
            elif value == target:
                return True
        subset_sums |= next_sums
    return False


def main():
    assert can_partition([1, 2, 3, 4]) is True
    assert can_partition([1, 1, 3, 4, 7]) is True
    assert can_partition([2, 3, 4, 6]) is False

    assert can_partition_top_down([1, 2, 3, 4]) is True
    assert can_partition_top_down([1, 1, 3, 4, 7]) is True
    assert can_partition_top_down([2, 3, 4, 6]) is False

    assert can_partition_bottom_up([1, 2, 3, 4]) is True
    assert can_partition_bottom_up([1, 1, 3, 4, 7]) is True
    assert can_partition_bottom_up([2, 3, 4, 6]) is False


main()
