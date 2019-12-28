from collections import Counter


def find_permutation(s: str, pattern: str) -> bool:
    if len(pattern) > len(s):
        return False

    delta = Counter(pattern)
    remaining_letters = set()
    for end in range(len(pattern)):
        delta[s[end]] -= 1
        if delta[s[end]] == 0:
            remaining_letters -= {s[end]}
        else:
            remaining_letters.add(s[end])

    if not remaining_letters:
        return True

    begin = 0
    for end in range(len(pattern), len(s)):
        delta[s[end]] -= 1
        if delta[s[end]] == 0:
            remaining_letters -= {s[end]}
        else:
            remaining_letters.add(s[end])

        delta[s[begin]] += 1
        if delta[s[begin]] == 0:
            remaining_letters -= {s[begin]}
        else:
            remaining_letters.add(s[begin])
        begin += 1
        if not remaining_letters:
            return True
    return False


assert find_permutation("oidbcaf", "abc")
assert not find_permutation("odicf", "dc")
assert find_permutation("bcdxabcdy", "bcdyabcdx")
assert find_permutation("aaacb", "abc")
