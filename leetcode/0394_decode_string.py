import string
from typing import Iterable


class Solution:
    def decodeString(self, s: str) -> str:
        def decode(encoded: str) -> str:
            """ This should end with a close bracket """
            i = find_first_digit(encoded)
            if i == -1:
                # This should already be decoded
                return encoded

            j = encoded.find("[", i)
            k = find_matching_bracket_from_index(encoded, j)
            inner = decode(helper(encoded[j + 1 : k]))
            return f"{encoded[:i]}{inner * int(encoded[i:j])}"

        def break_into_groups(encoded: str) -> Iterable[str]:
            groups = []
            i = 0
            while i < len(encoded):
                first_open_bracket = encoded.find("[", i)
                if first_open_bracket == -1:
                    groups.append(encoded[i:])
                    break
                close_open_bracket = find_matching_bracket_from_index(
                    encoded, first_open_bracket
                )
                groups.append(encoded[i : close_open_bracket + 1])
                i = close_open_bracket + 1
            return groups

        def helper(encoded: str) -> str:
            groups = break_into_groups(encoded)
            if len(groups) == 1:
                return decode(groups[0])
            return "".join(map(helper, groups))

        return helper(s)


def find_first_digit(s: str) -> int:
    for i, c in enumerate(s):
        if c in string.digits:
            return i
    return -1


def find_matching_bracket_from_index(s: str, i: int) -> int:
    assert s[i] == "[", "You are misusing this function"
    brackets = 1
    while brackets > 0:
        i += 1
        if s[i] == "[":
            brackets += 1
        elif s[i] == "]":
            brackets -= 1
    return i


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("3[a]2[b4[F]c]"))
print(Solution().decodeString("zzzyypq4[2[jk]e1[f]]yypq4[2[jk]e1[f]]ef"))
