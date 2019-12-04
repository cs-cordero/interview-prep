from bisect import bisect_left, insort
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        seen = set()
        best = float("inf")
        for i in range(len(nums) - 2):
            num = nums[i]
            if num in seen:
                continue
            seen.add(num)

            subtarget = target - num
            sorted_arr = []
            for j in range(i + 1, len(nums)):
                current = nums[j]
                if sorted_arr:
                    ideal_pair = subtarget - current
                    bisection = min(
                        bisect_left(sorted_arr, ideal_pair), len(sorted_arr) - 1
                    )
                    candidates = [num + current + sorted_arr[bisection]]
                    if bisection > 0:
                        candidates.append(num + current + sorted_arr[bisection - 1])
                    for candidate in candidates:
                        if candidate == target:
                            return target
                        elif abs(candidate - target) < abs(best - target):
                            best = candidate
                insort(sorted_arr, current)
        return best
