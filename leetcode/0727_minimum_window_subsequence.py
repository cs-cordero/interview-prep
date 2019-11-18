class Solution:
    def minWindow(self, S: str, T: str) -> str:
        dp = [[None for _ in range(len(S) + 1)] for _ in range(len(T) + 1)]
        for i in range(len(S) + 1):
            dp[0][i] = i

        for t_i, t in enumerate(T, 1):
            for s_i, s in enumerate(S, 1):
                if t != s:
                    dp[t_i][s_i] = dp[t_i][s_i - 1]
                elif dp[t_i - 1][s_i - 1] is not None:
                    dp[t_i][s_i] = dp[t_i - 1][s_i - 1]

        best = None
        for i, value in enumerate(dp[-1]):
            if value is None:
                continue
            substring = S[value:i]
            if best is None or len(best) > len(substring):
                best = substring
        return best or ""


print(Solution().minWindow(S="abcdebdde", T="bde"))
print(Solution().minWindow(S="cnhczmccqouqadqtmjjzl", T="mm"))
