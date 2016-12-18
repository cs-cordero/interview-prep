class Solution:
    def isNumber(self, s: str) -> bool:
        allow_decimal = True
        allow_exponent = False
        allow_leading_space = True
        allow_sign = True

        seen_exponent = False
        seen_decimal = False
        seen_number = False

        cannot_end = True

        for character in s.strip():
            if character == " " and allow_leading_space:
                cannot_end = False

            elif character in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                allow_decimal = not seen_decimal and not seen_exponent
                allow_exponent = not seen_exponent
                allow_leading_space = False
                allow_sign = False
                cannot_end = False
                seen_number = True

            elif character == "e" and allow_exponent:
                allow_decimal = False
                allow_exponent = False
                allow_leading_space = False
                allow_sign = True
                seen_exponent = True
                seen_number = False
                cannot_end = True

            elif character in {"+", "-"} and allow_sign:
                allow_decimal = True
                allow_exponent = False
                allow_leading_space = False
                allow_sign = False
                cannot_end = True

            elif character == "." and allow_decimal:
                allow_decimal = False
                allow_exponent = not seen_exponent and seen_number
                allow_leading_space = False
                allow_sign = False
                seen_decimal = True
                cannot_end = not seen_number

            else:
                return False
        return not cannot_end


assert Solution().isNumber("0") is True
assert Solution().isNumber(" 0.1 ") is True
assert Solution().isNumber("abc") is False
assert Solution().isNumber("1 a") is False
assert Solution().isNumber("2e10") is True
assert Solution().isNumber(" -90e3   ") is True
assert Solution().isNumber(" 1e") is False
assert Solution().isNumber("e3") is False
assert Solution().isNumber(" 6e-1") is True
assert Solution().isNumber(" 99e2.5 ") is False
assert Solution().isNumber("53.5e93") is True
assert Solution().isNumber(" --6 ") is False
assert Solution().isNumber("-+3") is False
assert Solution().isNumber("95a54e53") is False
assert Solution().isNumber(".1") is True
assert Solution().isNumber("3.") is True
assert Solution().isNumber(".") is False
assert Solution().isNumber("+.8") is True
assert Solution().isNumber("46.e3") is True
assert Solution().isNumber(".e1") is False
assert Solution().isNumber("7.e-.") is False
