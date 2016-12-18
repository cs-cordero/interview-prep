from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counts = Counter(s)
            hash_value = frozenset(f"{char}{count}" for char, count in counts.items())
            groups[hash_value].append(s)
        return list(groups.values())
