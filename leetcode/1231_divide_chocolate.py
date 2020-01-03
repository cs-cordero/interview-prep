from typing import List, Optional


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def helper(k: int, minimum: int) -> Optional[int]:
            current = 0
            least_sweet = float("inf")
            for sweet in sweetness:
                current += sweet
                if current >= minimum:
                    least_sweet = min(least_sweet, current)
                    current = 0
                    k -= 1
                    if k == 0:
                        break
            return least_sweet if k == 0 else None

        left, right = min(sweetness), sum(sweetness)
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            least_sweet = helper(K + 1, mid)
            if least_sweet is None:
                # could not generate enough groups
                # minimum is too high
                right = mid - 1
            else:
                # mid was a small enough minimum to
                # generate at least enough groups.
                answer = max(answer, least_sweet)
                left = mid + 1
        return answer
