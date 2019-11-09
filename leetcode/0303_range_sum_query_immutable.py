from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sums = [0]
        running_count = 0
        for num in nums:
            running_count += num
            self.prefix_sums.append(running_count)

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sums[j + 1] - self.prefix_sums[i]
