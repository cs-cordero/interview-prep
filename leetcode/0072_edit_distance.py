class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[None for _ in range(len(word2))] for _ in range(len(word1))]

        def match(i: int, j: int) -> int:
            if i >= len(word1):
                return len(word2) - j
            elif j >= len(word2):
                return len(word1) - i
            elif dp[i][j] is not None:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = match(i + 1, j + 1)
            else:
                dp[i][j] = (
                    min(match(i + 1, j + 1), match(i + 1, j), match(i, j + 1)) + 1
                )
            return dp[i][j]

        return match(0, 0)


assert Solution().minDistance("horse", "ros") == 3
assert Solution().minDistance("hello", "world") == 4
assert Solution().minDistance("intention", "execution") == 5
assert Solution().minDistance("prosperity", "properties") == 4
assert Solution().minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine") == 6
assert (
    Solution().minDistance("trinitrophenylmethylnitramine", "dinitrophenylhydrazine")
    == 10
)
assert Solution().minDistance("zoologicoarchaeologist", "zoogeologist") == 10
