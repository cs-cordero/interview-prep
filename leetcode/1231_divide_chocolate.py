from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def helper(target: int) -> int:
            groups = 1
            running_total = 0
            for sweet in sweetness:
                running_total += sweet
                if running_total >= target:
                    groups += 1
                    running_total = 0
            return groups

        left = 0
        right = sum(sweetness)
        while left <= right:
            mid = (left + right) // 2
            groups = helper(mid)
            if groups > K + 1:
                left = mid + 1
            else:
                right = mid - 1
        return right


print(
    Solution().maximizeSweetness(
        [90670, 55382, 95298, 95795, 73204, 41464, 18675, 30104, 47442, 55307], 6
    )
)
