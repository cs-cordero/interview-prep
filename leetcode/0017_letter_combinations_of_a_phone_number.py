from itertools import product
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        result = list(mapping[digits[0]])
        for digit in digits[1:]:
            result = ["".join(value) for value in product(result, mapping[digit])]
        return result
