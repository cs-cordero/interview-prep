from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def count_subarrays(target: int) -> int:
            subarrays = 0
            highest_count_in_subarray = 0
            count = 0
            for num in nums:
                if count + num > target:
                    highest_count_in_subarray = max(highest_count_in_subarray, count)
                    count = num
                    subarrays += 1
                else:
                    count += num

            highest_count_in_subarray = max(highest_count_in_subarray, count)
            return subarrays + 1, highest_count_in_subarray

        left = 0
        right = sum(nums)
        results = {}
        while left < right:
            mid = (left + right) // 2
            subarray_count, highest_count_in_subarray = count_subarrays(mid)
            if subarray_count > m:
                left = mid + 1
            else:
                right = mid
            if subarray_count == m:
                results[mid] = highest_count_in_subarray
        return min(results.values())
