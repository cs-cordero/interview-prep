import random
from itertools import zip_longest

ADD_MAP = {(str(i), str(j)): str(i + j) for i in range(10) for j in range(10)}

MUL_MAP = {(str(i), str(j)): str(i * j) for i in range(10) for j in range(10)}


class Solution:
    """
    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You *must not use any built-in BigInteger library*
        or *convert the inputs* to integer directly.
    """

    def multiply(self, num1: str, num2: str) -> str:
        return multiply_as_str(num1, num2)


def add_as_str(num1: str, num2: str) -> str:
    value = ""
    remainder = ""
    for a, b in zip_longest(reversed(num1), reversed(num2), fillvalue="0"):
        raw_added = ADD_MAP[(a, b)]
        if remainder and remainder != "0":
            raw_added = add_as_str(raw_added, remainder)
        remainder = raw_added[:-1]
        value += raw_added[-1]
    if remainder:
        value += remainder
    return value[::-1]


def multiply_as_str(multiplicand: str, multiplier: str) -> str:
    if multiplicand == "0" or multiplier == "0":
        return "0"
    elif multiplicand == "1":
        return multiplier
    elif multiplier == "1":
        return multiplicand

    values = []
    for extra_zeros, b in enumerate(reversed(multiplier)):
        value = ""
        remainder = ""
        for a in reversed(multiplicand):
            raw_multiplied = MUL_MAP[(a, b)]
            if remainder and remainder != "0":
                raw_multiplied = add_as_str(raw_multiplied, remainder)
            remainder = raw_multiplied[:-1]
            value += raw_multiplied[-1]
        if remainder:
            value += remainder
        value = value[::-1]
        value += "0" * extra_zeros
        values.append(value)

    result = "0"
    for value in values:
        result = add_as_str(result, value)
    return result


for _ in range(1000):
    a = random.randint(0, 9999999)
    b = random.randint(0, 9999999)
    answer = Solution().multiply(str(a), str(b))
    assert answer == str(a * b), f"{a} * {b} = {answer} != {a*b}"
