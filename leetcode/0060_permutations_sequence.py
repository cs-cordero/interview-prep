from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = ""
        numbers = [num + 1 for num in range(n)]
        k -= 1
        while numbers:
            divisor = factorial(len(numbers) - 1) if len(numbers) > 1 else 0
            i = k // divisor if divisor > 0 else 0
            s += str(numbers.pop(i))
            k -= i * divisor
        return s


print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(4, 9))
