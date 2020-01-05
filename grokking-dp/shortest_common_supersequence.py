def find_SCS_length(s1: str, s2: str) -> int:
    lcs_length = lcs(s1, s2)
    return len(s1) - lcs_length + len(s2) - lcs_length + lcs_length


def lcs(s1: str, s2: str) -> int:
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i, char1 in enumerate(s1, 1):
        for j, char2 in enumerate(s2, 1):
            if char1 == char2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def main():
    print(find_SCS_length("abcf", "bdcf"))
    print(find_SCS_length("dynamic", "programming"))


main()
