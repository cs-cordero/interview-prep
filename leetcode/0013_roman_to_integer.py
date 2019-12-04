from typing import Iterable


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,
        }

        def romans() -> Iterable[int]:
            i = 0
            while i < len(s):
                if s[i : i + 2] in symbol_map:
                    yield symbol_map[s[i : i + 2]]
                    i += 2
                else:
                    yield symbol_map[s[i]]
                    i += 1

        return sum(roman for roman in romans())
