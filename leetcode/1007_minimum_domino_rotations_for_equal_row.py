from collections import defaultdict
from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        countsA = defaultdict(int)
        countsB = defaultdict(int)

        possible = None
        for a, b in zip(A, B):
            if possible is None:
                possible = {a, b}
            else:
                possible &= {a, b}
            if not possible:
                return -1
            countsA[a] += a != b
            countsB[b] += a != b

        value = next(iter(possible))
        return min(countsA[value], countsB[value])
