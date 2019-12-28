from collections import Counter


def find_substring(s: str, pattern: str):
    pattern_counts = Counter(pattern)
    begin = 0
    remaining = set(pattern_counts.keys())
    best = None
    for end, character in enumerate(s):
        if character not in pattern_counts:
            continue

        pattern_counts[character] -= 1
        if pattern_counts[character] == 0:
            remaining -= {character}

        while not remaining:
            candidate = s[begin : end + 1]
            best = candidate if best is None or len(candidate) < len(best) else best
            removed_char = s[begin]
            if removed_char in pattern_counts:
                pattern_counts[removed_char] += 1
                if pattern_counts[removed_char] > 0:
                    remaining |= {removed_char}
            begin += 1
    return best or ""


assert find_substring("aabdec", "abc") == "abdec"
assert find_substring("abdabca", "abc") == "abc"
assert find_substring("adcad", "abc") == ""
