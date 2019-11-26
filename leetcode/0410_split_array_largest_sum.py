from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def count_chunks(k: int) -> int:
            chunks = 0
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum >= k:
                    chunks += 1
                if current_sum > k:
                    current_sum = num
                elif current_sum == k:
                    current_sum = 0
            if current_sum > 0 and current_sum <= k:
                chunks += 1
            return chunks

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            chunks = count_chunks(mid)
            if chunks <= m:
                right = mid
            else:
                left = mid + 1
        return right
