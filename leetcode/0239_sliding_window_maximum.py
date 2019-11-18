from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        window = deque()

        def monotonic_append_with_index(i: int) -> None:
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)

        for i in range(k):
            monotonic_append_with_index(i)

        result.append(nums[window[0]])

        for j in range(k, len(nums)):
            if window and window[0] <= j - k:
                window.popleft()
            monotonic_append_with_index(j)
            result.append(nums[window[0]])
        return result
