from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        chains = Counter()

        for num in nums:
            if counts[num] == 0:
                continue

            can_add_to_previous_chain = chains[num - 1] > 0
            can_start_new_chain = all(
                counts[number] > 0 for number in (num, num + 1, num + 2)
            )

            counts[num] -= 1
            if can_add_to_previous_chain:
                chains[num - 1] -= 1
                chains[num] += 1
            elif can_start_new_chain:
                counts[num + 1] -= 1
                counts[num + 2] -= 1
                chains[num + 2] += 1
            else:
                return False
        return True
