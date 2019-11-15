from collections import Counter
from itertools import zip_longest


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counts = Counter(secret)
        misses = Counter()

        bulls = 0
        for a, b in zip_longest(secret, guess):
            if a == b:
                bulls += 1
                counts[b] -= 1
            else:
                misses[b] += 1

        cows = 0
        for char, count in misses.items():
            cows += min(count, counts[char])
        return f"{bulls}A{cows}B"
