class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0

        for place, a_str in enumerate(reversed(num1)):
            a = int(a_str)
            remainder = 0
            for inner_place, b_str in enumerate(reversed(num2)):
                b = int(b_str)
                temp = a * b + remainder
                remainder, digit = temp // 10, temp % 10
                result += digit * (10 ** inner_place) * (10 ** place)
            if remainder:
                result += remainder * (10 ** (inner_place + 1)) * (10 ** place)
        return str(result)
