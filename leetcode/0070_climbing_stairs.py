class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        a, b = 1, 1
        for _ in range(2, n + 1):
            b, a = a + b, b
        return b


print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
