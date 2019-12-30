from typing import List


class Solution:
    def intervalIntersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:
        result = []
        a = 0
        b = 0
        while a < len(A) and b < len(B):
            a_start, a_end = A[a]
            b_start, b_end = B[b]
            if a_start <= b_end and a_end >= b_start:
                result.append([max(a_start, b_start), min(a_end, b_end)])

            if a_end <= b_end:
                a += 1
            else:
                b += 1
        return result
