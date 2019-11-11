from typing import List, Tuple


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        letters, counts = get_stretchable_groups(S)

        def can_be_expressed(word: str) -> bool:
            pointer_s = 0
            pointer_word = 0

            while pointer_word < len(word) and pointer_s < len(letters):
                current_letter = word[pointer_word]

                if current_letter != letters[pointer_s]:
                    return False

                current_count = 0
                while pointer_word < len(word) and word[pointer_word] == current_letter:
                    current_count += 1
                    pointer_word += 1

                counts_match = counts[pointer_s] == current_count
                can_expand_into_s = (
                    counts[pointer_s] >= 3 and current_count < counts[pointer_s]
                )
                if counts_match or can_expand_into_s:
                    pointer_s += 1
                    continue

                return False

            return pointer_s == len(letters)

        return sum(can_be_expressed(word) for word in words)


def get_stretchable_groups(word: str) -> Tuple[List[str], List[bool]]:
    letters = []
    counts = []
    if not word:
        return letters, counts

    current_letter = word[0]
    current_count = 1
    for letter in word[1:]:
        if letter == current_letter:
            current_count += 1
        else:
            letters.append(current_letter)
            counts.append(current_count)
            current_count = 1
            current_letter = letter

    if not letters or current_letter != letters[-1]:
        letters.append(current_letter)
        counts.append(current_count)

    return letters, counts
