class Solution:
    def intToRoman(self, num: int) -> str:
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

        roman = ""
        for symbol, value in symbol_map.items():
            while value <= num:
                roman += symbol
                num -= value
        return roman


print(Solution().intToRoman(3))
print(Solution().intToRoman(4))
print(Solution().intToRoman(9))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
