WORD_MAP = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}

TENS_MAP = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}

PLACE_MAP = ["Thousand", "Million", "Billion", "Trillion"]


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return WORD_MAP[num]

        result = []

        first_two_digits = WORD_MAP.get(num % 100)
        if not first_two_digits:
            ones = WORD_MAP[num % 10]
            num //= 10
            tens = TENS_MAP[num % 10]
            num //= 10
            first_two_digits = f"{tens} {ones}" if ones != "Zero" else tens
        else:
            num //= 100

        if first_two_digits != "Zero":
            result.append(first_two_digits)

        hundreds = WORD_MAP[num % 10]
        if hundreds != "Zero":
            result.append(f"{hundreds} Hundred")
        num //= 10

        if num == 0:
            return " ".join(reversed(result))

        place = 0
        while num:
            next_group = self.numberToWords(num % 1000)
            next_place = PLACE_MAP[place]

            if next_group != "Zero":
                result.append(f"{next_group} {next_place}")
            num //= 1000
            place += 1
        return " ".join(reversed(result))


print(Solution().numberToWords(0))
print(Solution().numberToWords(1))
print(Solution().numberToWords(12))
print(Solution().numberToWords(112))
print(Solution().numberToWords(1112))
print(Solution().numberToWords(1234567))
print(Solution().numberToWords(10))
print(Solution().numberToWords(100))
print(Solution().numberToWords(1000))
print(Solution().numberToWords(10000))
print(Solution().numberToWords(100000))
print(Solution().numberToWords(1000000))
