from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()

        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1

        unique_numbers = list(mapping.keys())
        for i, i_num in enumerate(unique_numbers):
            for j in range(i, len(unique_numbers)):
                j_num = unique_numbers[j]
                if j_num == i_num and mapping[j_num] < 2:
                    continue

                needed_num = 0 - i_num - j_num
                needed_count = 1 + (needed_num == i_num) + (needed_num == j_num)
                if mapping[needed_num] >= needed_count:
                    results.add(tuple(sorted([i_num, j_num, needed_num])))

        return [list(combo) for combo in results]
