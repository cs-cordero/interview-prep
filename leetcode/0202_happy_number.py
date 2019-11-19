class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            number = 0
            while n:
                number += (n % 10) ** 2
                n //= 10
            if number == 1:
                return True
            if number in seen:
                return False
            seen.add(number)
            n = number
