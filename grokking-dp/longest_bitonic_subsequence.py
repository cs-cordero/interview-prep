from typing import List


def find_LBS_length(nums: List[int]) -> int:
    increasing = [1] * len(nums)
    decreasing = [0] * len(nums)

    lbs = 0
    for i in range(1, len(nums)):
        current_num = nums[i]
        best_increasing_index = -1
        best_decreasing_index = -1
        for j in range(i):
            previous_num = nums[j]
            if previous_num < current_num:
                is_unset = best_increasing_index == -1
                is_better = (
                    is_unset or increasing[best_increasing_index] < increasing[j]
                )
                if is_better:
                    best_increasing_index = j

            if previous_num > current_num:
                is_unset = best_decreasing_index == -1
                value_from_increasing = increasing[j]
                value_from_decreasing = decreasing[j]
                best_value = max(value_from_increasing, value_from_decreasing)
                is_better = (
                    is_unset
                    or max(
                        increasing[best_decreasing_index],
                        decreasing[best_decreasing_index],
                    )
                    < best_value
                )
                if is_better:
                    best_decreasing_index = j

        if best_increasing_index != -1:
            increasing[i] = increasing[best_increasing_index] + 1
        if best_decreasing_index != -1:
            decreasing[i] = (
                max(
                    decreasing[best_decreasing_index], increasing[best_decreasing_index]
                )
                + 1
            )
            lbs = max(lbs, decreasing[i])

    print(nums)
    print(increasing)
    print(decreasing)
    return lbs


def main():
    print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
    print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))


main()

"""
 4  2  3  6 10  1 12
[1  1  2  3  4  1  5] increasing
[0  2  2  0  0  5  0] decreasing
"""
