from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, character in enumerate(s):
            if counts[character] == 1:
                return i
        return -1
