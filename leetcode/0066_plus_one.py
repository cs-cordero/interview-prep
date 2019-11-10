from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + 1
            digit, remainder = temp % 10, temp // 10
            digits[i] = digit
            if not remainder:
                return digits

        digits.insert(0, remainder)
        return digits
