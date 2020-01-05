class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [None for _ in range(len(s))]

        def helper(i: int) -> int:
            if i >= len(s):
                return 1
            if dp[i] is not None:
                return dp[i]

            value = int(s[i])
            supports_single_digit = "0" not in s[i : i + 2]
            supports_double_digit = i < len(s) - 1 and (
                value == 1 or (value == 2 and int(s[i + 1]) <= 6)
            )

            dp[i] = 0
            if supports_single_digit:
                dp[i] += helper(i + 1)

            if supports_double_digit:
                dp[i] += helper(i + 2)

            return dp[i]

        return helper(0)


print(Solution().numDecodings("01"))
print(Solution().numDecodings("0"))
print(Solution().numDecodings("100"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("27"))
print(Solution().numDecodings("111112326222"))
