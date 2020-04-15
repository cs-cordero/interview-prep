from collections import Counter, defaultdict
from typing import List


def serialize_counter(counter: Counter) -> str:
    return "".join(f"{letter}{count}" for letter, count in sorted(counter.items()))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[serialize_counter(Counter(s))].append(s)
        return list(groups.values())
