from bisect import bisect
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def get_frequency(word: str) -> int:
            smallest_letter = "z"
            frequency = 0
            for letter in word:
                if letter < smallest_letter:
                    smallest_letter = letter
                    frequency = 1
                elif letter == smallest_letter:
                    frequency += 1
            return frequency

        word_freqs = sorted([get_frequency(word) for word in words])
        return [
            len(words) - bisect(word_freqs, get_frequency(query)) for query in queries
        ]
