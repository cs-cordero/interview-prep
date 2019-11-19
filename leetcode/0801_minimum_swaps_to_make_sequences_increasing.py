from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        prev_swaps = 1
        prev_noswaps = 0

        for i, (a, b) in enumerate(zip(A, B)):
            if i == 0:
                continue
            swaps = float("inf")
            noswaps = float("inf")

            if A[i - 1] < a and B[i - 1] < b:
                noswaps = min(noswaps, prev_noswaps)
                swaps = min(swaps, prev_swaps + 1)
            if A[i - 1] < b and B[i - 1] < a:
                swaps = min(swaps, prev_noswaps + 1)
                noswaps = min(noswaps, prev_swaps)

            prev_swaps = swaps
            prev_noswaps = noswaps
        return min(prev_swaps, prev_noswaps)


print(Solution().minSwap([1, 3, 5, 4], [1, 2, 3, 7]))
