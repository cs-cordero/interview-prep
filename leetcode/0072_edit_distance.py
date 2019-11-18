class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(len(word2) + 1):
            dp[0][i] = i

        for i, word1_character in enumerate(word1, 1):
            for j, word2_character in enumerate(word2, 1):
                if word1_character != word2_character:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]
