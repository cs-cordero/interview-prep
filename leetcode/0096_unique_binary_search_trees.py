class Solution:
    def numTrees(self, n: int) -> int:
        dp = [None for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            local_answer = 0
            for j in range(i):
                local_answer += dp[i - j - 1] * dp[j]
            dp[i] = local_answer

        return dp[-1]
