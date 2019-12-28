from collections import Counter
from typing import List


def find_word_concatenation(s: str, words: List[str]) -> List[int]:
    result = []

    if not s or not words:
        return result

    reference_counts = Counter(words)
    word_len = len(words[0])

    for start in range(word_len):
        begin = start
        counts = Counter()
        required = len(reference_counts)
        for end in range(begin, len(s), word_len):
            current_word = s[end : end + word_len]
            if current_word not in reference_counts:
                required = len(reference_counts)
                begin = end + word_len
                counts.clear()
                continue

            while counts[current_word] == reference_counts[current_word]:
                removed_word = s[begin : begin + word_len]
                if counts[removed_word] == reference_counts[removed_word]:
                    required += 1
                counts[removed_word] -= 1
                begin += word_len

            counts[current_word] += 1
            if counts[current_word] == reference_counts[current_word]:
                required -= 1

            if not required:
                result.append(begin)
    return result
