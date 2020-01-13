from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def helper(target: int) -> bool:
            current = 0
            buckets = 0
            for i in range(len(sweetness)):
                if current + sweetness[i] >= target:
                    current = 0
                    buckets += 1
                else:
                    current += sweetness[i]
            return buckets >= K + 1

        total = sum(sweetness)
        left = 0
        right = total // (K + 1)
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right


print(Solution().maximizeSweetness([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
print(Solution().maximizeSweetness([5, 6, 7, 8, 9, 1, 2, 3, 4], 8))
