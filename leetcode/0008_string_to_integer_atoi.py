import string


class Solution:
    def myAtoi(self, s: str) -> int:
        raw, *_ = s.strip().split(" ")

        sign = 1
        if raw and raw[0] in ("-", "+"):
            sign = -1 if raw[0] == "-" else 1
            raw = raw[1:]

        if not raw:
            return 0

        for end, character in enumerate(raw):
            if character not in string.digits:
                break
        else:
            end += 1

        INT_MAX = 2 ** 31 - 1
        INT_MIN = (-2) ** 31
        value = 0
        try:
            value = sign * int(raw[:end])
        except ValueError:
            pass
        return min(max(INT_MIN, value), INT_MAX)
