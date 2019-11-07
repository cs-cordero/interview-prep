from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def splitting_method(largest_subarray_allowed: int) -> bool:
            buckets = 0
            current = 0
            for num in nums:
                if current + num > largest_subarray_allowed:
                    current = 0
                    buckets += 1
                current += num
            if current > 0:
                buckets += 1
            return buckets <= m

        left = max(nums)
        right = sum(nums)
        result = right
        while left < right:
            mid = (left + right) // 2
            if splitting_method(mid):
                result = min(result, mid)
                right = mid
            else:
                left = mid + 1
        return result


foo = [7, 2, 5, 10, 8]
print(Solution().splitArray(foo, 3))
