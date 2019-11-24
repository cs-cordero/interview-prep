from collections import Counter, defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            counts = Counter(word)
            serialized = "".join(
                f"{letter}{counts[letter]}"
                for letter in "abcdefghijklmnopqrstuvwxyz"
                if letter in counts
            )
            groups[serialized].append(word)
        return list(groups.values())
