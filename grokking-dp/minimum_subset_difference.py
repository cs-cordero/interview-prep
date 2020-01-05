from typing import List


def can_partition(nums: List[int]) -> int:
    def helper(i: int, difference: int) -> int:
        if i == len(nums):
            return abs(difference)
        return min(
            helper(i + 1, difference + nums[i]), helper(i + 1, difference - nums[i])
        )

    return helper(0, 0)


def can_partition_bottom_up(nums: List[int]) -> int:
    subset_sums = {0}
    for num in nums:
        next_sums = set()
        for subset_sum in subset_sums:
            next_sums.add(subset_sum + num)
            next_sums.add(subset_sum - num)
        subset_sums = next_sums
    return min(abs(value) for value in subset_sums)


def can_partition_bottom_up_space_optimized(nums: List[int]) -> int:
    total = sum(nums)
    target = total // 2
    target += 1 if total % 2 != 0 else 0

    subset_sums = {0}
    for num in nums:
        next_sums = set()
        for subset_sum in subset_sums:
            value = subset_sum + num
            if value > target:
                continue
            next_sums.add(value)
        subset_sums |= next_sums
    return total - 2 * max(subset_sums)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))

    print("Can partition: " + str(can_partition_bottom_up([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition_bottom_up([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition_bottom_up([1, 3, 100, 4])))

    print(
        "Can partition: " + str(can_partition_bottom_up_space_optimized([1, 2, 3, 9]))
    )
    print(
        "Can partition: "
        + str(can_partition_bottom_up_space_optimized([1, 2, 7, 1, 5]))
    )
    print(
        "Can partition: " + str(can_partition_bottom_up_space_optimized([1, 3, 100, 4]))
    )


main()
