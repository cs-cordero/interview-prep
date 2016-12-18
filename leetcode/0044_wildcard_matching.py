class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_i = 0
        p_i = 0

        while (s_i < len(s) and p_i < len(p)) and (s[s_i] == p[p_i] or p[p_i] == "?"):
            s_i += 1
            p_i += 1

        consumed_s = s_i >= len(s)
        consumed_p = p_i >= len(p)
        if consumed_s and consumed_p:
            # Consumed both s and p, so it's a match.
            return True
        elif consumed_s or consumed_p:
            # Special case where p is not consumed,
            # but the last one is a * or a series of *
            if not consumed_p and all(remaining == "*" for remaining in p[p_i:]):
                return True

            # Consumed one or the other, but not both, so it's not a match.
            return False

        p_char = p[p_i]
        if p_char != "*":
            # No match and it wasn't because we hit a wildcard
            return False

        # Scan for a wildcard end character
        found_wildcard_end = False
        while p_i < len(p):
            p_char = p[p_i]
            if p_char != "*":
                found_wildcard_end = True
                break
            p_i += 1

        if not found_wildcard_end:
            # wildcard will match the rest of the string
            return True

        # Recurse
        remaining_p = p[p_i:]
        remaining_non_wildcard_block_length = 1
        for remaining_non_wildcard_block_length in range(1, len(remaining_p)):
            if remaining_p[remaining_non_wildcard_block_length] in ("?", "*"):
                break
        next_p_block = remaining_p[:remaining_non_wildcard_block_length]
        if next_p_block == "aaaaaaaaa":
            breakpoint()
        for next_s in range(s_i, len(s)):
            if next_p_block != s[next_s : next_s + remaining_non_wildcard_block_length]:
                continue

            if (
                next_p_block
                != s[next_s + 1 : next_s + remaining_non_wildcard_block_length + 1]
            ):
                continue

            if self.isMatch(s[next_s:], remaining_p):
                return True
        return False


def run_test(data, expected):
    result = Solution().isMatch(*data)
    assert result == expected, expected


run_test(("aa", "a"), False)
run_test(("aa", "*"), True)
run_test(("cb", "?a"), False)
run_test(("adceb", "a*b"), True)
run_test(("acdcb", "a*c?b"), False)
run_test(("abefcdgiescdfimde", "ab*cd?i*de"), True)
run_test(("", "*"), True)
run_test(("a", "a*"), True)
run_test(
    (
        "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
        "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb",
    ),
    False,
)
