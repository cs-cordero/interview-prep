def find_LCS_length(s1: str, s2: str) -> int:
    dp = [[None for _ in range(len(s2))] for _ in range(len(s1))]

    def helper(i: int, j: int) -> int:
        if i == len(s1) or j == len(s2):
            return 0

        if dp[i][j] is None:
            if s1[i] == s2[j]:
                dp[i][j] = 1 + helper(i + 1, j + 1)
            else:
                dp[i][j] = max(helper(i + 1, j), helper(i, j + 1))
        return dp[i][j]

    return helper(0, 0)


def find_LCS_length_bottom_up(s1: str, s2: str) -> int:
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i, c1 in enumerate(s1, 1):
        for j, c2 in enumerate(s2, 1):
            if c1 == c2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))

    print(find_LCS_length_bottom_up("abdca", "cbda"))
    print(find_LCS_length_bottom_up("passport", "ppsspt"))


main()
