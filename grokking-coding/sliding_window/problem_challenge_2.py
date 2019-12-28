from collections import Counter
from typing import List


def find_string_anagrams(s: str, pattern: str) -> List:
    count = Counter()
    pattern_count = Counter(pattern)
    delta = set(pattern_count.keys())
    result_indexes = []

    begin = 0
    for end, character in enumerate(s):
        count[character] += 1
        if count[character] == pattern_count[character]:
            delta -= {character}

        while end - begin + 1 > len(pattern):
            removed_char = s[begin]
            count[removed_char] -= 1
            if count[removed_char] != pattern_count[removed_char]:
                delta |= {removed_char}
            begin += 1

        if not delta:
            result_indexes.append(begin)

    return result_indexes


assert find_string_anagrams("ppqp", "pq") == [1, 2]
assert find_string_anagrams("abbcabc", "abc") == [2, 3, 4]
assert find_string_anagrams("ab", "abc") == []
