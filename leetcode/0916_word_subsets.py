from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counts_B = Counter()
        for b in B:
            for letter, count in Counter(b).items():
                counts_B[letter] = max(counts_B[letter], count)

        def is_subset(a: Counter) -> bool:
            return all(value <= a[key] for key, value in counts_B.items())

        return [a for a in A if is_subset(Counter(a))]
