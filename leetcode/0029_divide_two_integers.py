class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        multiplicand = 0
        counter = 0
        steps = 0
        stay_positive = (dividend < 0 and divisor < 0) or (
            dividend >= 0 and divisor >= 0
        )
        dividend = abs(dividend)
        divisor = abs(divisor)

        while counter < dividend:
            counter += divisor + (divisor * steps)
            multiplicand += steps + 1
            steps += 1
        while counter > dividend:
            counter -= divisor
            multiplicand -= 1

        if multiplicand > 2147483647:
            # force the answer to stay within 32 bytes
            multiplicand = 2147483647 if stay_positive else 2147483648

        return multiplicand if stay_positive else -multiplicand


assert Solution().divide(10, 2) == 5
assert Solution().divide(2, 2) == 1
assert Solution().divide(3, 2) == 1
assert Solution().divide(4, 2) == 2
assert Solution().divide(4, 3) == 1
assert Solution().divide(-10, 2) == -5
assert Solution().divide(-2, 2) == -1
assert Solution().divide(-3, 2) == -1
assert Solution().divide(-4, 2) == -2
assert Solution().divide(-4, 3) == -1
assert Solution().divide(-10, -2) == 5
