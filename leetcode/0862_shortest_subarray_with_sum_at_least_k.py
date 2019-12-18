from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix_sums = [0]
        for num in A:
            prefix_sums.append(prefix_sums[-1] + num)

        result = float("inf")
        queue = deque()
        for i, value in enumerate(prefix_sums):
            while queue and prefix_sums[queue[-1]] > value:
                queue.pop()

            while queue and value - prefix_sums[queue[0]] >= K:
                result = min(result, i - queue.popleft())

            queue.append(i)
        return result if result != float("inf") else -1
