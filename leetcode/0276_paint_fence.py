class Solution:
    def numWays(self, n: int, k: int) -> int:
        if not n:
            return 0

        combinations_in_state1 = k
        combinations_in_state2 = 0
        n -= 1

        for _ in range(n):
            temp = combinations_in_state2 * (k - 1)
            combinations_in_state2 = combinations_in_state1
            combinations_in_state1 *= k - 1
            combinations_in_state1 += temp
        return combinations_in_state1 + combinations_in_state2
