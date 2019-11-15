class Solution:
    def reverse(self, x: int) -> int:
        reversed_number = 0
        should_be_negative = x < 0
        x = abs(x)
        while x:
            reversed_number *= 10
            reversed_number += x % 10
            x //= 10
        reversed_number = -reversed_number if should_be_negative else reversed_number
        if -(2 ** 31) <= reversed_number and 2 ** 31 - 1 >= reversed_number:
            return reversed_number
        return 0
