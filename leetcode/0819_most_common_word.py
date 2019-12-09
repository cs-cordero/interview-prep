import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cleaned = re.sub(r"[!?',;.]", " ", paragraph).lower().split(" ")
        banned_words = set(banned)

        best_word = None
        best_freq = 0
        counts = Counter(cleaned)
        for word, freq in counts.items():
            if not word or word in banned_words:
                continue
            if freq > best_freq:
                best_freq = freq
                best_word = word
        return best_word
