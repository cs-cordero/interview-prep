from typing import List


def find_target_subsets(nums: List[int], s: int) -> int:
    def helper(i: int, current: int) -> int:
        if i == len(nums):
            return int(current == s)
        return helper(i + 1, current - nums[i]) + helper(i + 1, current + nums[i])

    return helper(0, 0)


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
