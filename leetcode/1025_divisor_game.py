from typing import Iterable


class Solution:
    def divisorGame(self, N: int) -> bool:
        if N <= 1:
            return False

        dp = [None] * (N + 1)
        dp[1] = False

        def can_win(i: int) -> bool:
            multiples = get_multiples(i)
            return any(dp[i - multiple] is False for multiple in multiples)

        def get_multiples(i: int) -> Iterable[int]:
            yield 1
            for multiple in range(2, i // 2 + 1):
                if i % multiple == 0:
                    yield multiple

        for n in range(2, N + 1):
            dp[n] = can_win(n)
        return dp[-1]


print(Solution().divisorGame(2))
print(Solution().divisorGame(3))
print(Solution().divisorGame(7))
print(Solution().divisorGame(8))
