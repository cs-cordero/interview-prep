from collections import defaultdict


def length_of_longest_substring(s: str, k: int) -> int:
    if not s:
        return 0

    counts = defaultdict(int)
    begin = 0
    result = 0
    for end in range(len(s)):
        window_size = end - begin
        counts[s[end]] += 1
        current_freq = counts[s[begin]]
        while window_size - current_freq + 1 > k:
            begin += 1
            window_size -= 1
            current_freq = counts[s[begin]]
        result = max(result, window_size + 1)
    return result


assert length_of_longest_substring("aabccbb", 2) == 5
assert length_of_longest_substring("abbcb", 1) == 4
assert length_of_longest_substring("abccde", 1) == 3
assert length_of_longest_substring("", 1) == 0
assert length_of_longest_substring("aabccbb", 0) == 2
