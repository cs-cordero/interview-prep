from collections import Counter
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counts = Counter(nums[:k])
        if any(count >= 2 for count in counts.values()):
            return True

        slow = 0
        fast = k
        while fast < len(nums):
            counts[nums[fast]] += 1
            if counts[nums[fast]] >= 2:
                return True
            counts[nums[slow]] -= 1
            slow += 1
            fast += 1
        return False
