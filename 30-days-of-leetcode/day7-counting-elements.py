from collections import Counter
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        freqs = Counter(arr)
        result = 0
        for number, freq in freqs.items():
            next_number = number + 1
            if next_number in freqs:
                result += freq
        return result
