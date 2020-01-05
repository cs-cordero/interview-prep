def find_LCS_length(s1: str, s2: str) -> int:
    dp = [[None for _ in range(len(s2))] for _ in range(len(s1))]

    def helper(i: int, j: int, count: int) -> int:
        if i == len(s1) or j == len(s2):
            return count

        if dp[i][j] is None or count >= dp[i][j]:
            if s1[i] == s2[j]:
                dp[i][j] = helper(i + 1, j + 1, count + 1)
            else:
                dp[i][j] = max(helper(i + 1, j, 0), helper(i, j + 1, 0))

        dp[i][j] = max(dp[i][j], count)
        return dp[i][j]

    return helper(0, 0, 0)


def find_LCS_length_bottom_up(s1: str, s2: str) -> int:
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    longest = 0
    for i, c1 in enumerate(s1, 1):
        for j, c2 in enumerate(s2, 1):
            if c1 == c2:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
            longest = max(longest, dp[i][j])
    return longest


def find_LCS_length_iterative(s1: str, s2: str) -> int:
    best = 0
    for i in range(len(s1)):
        current = 0
        k = i
        for j, c2 in enumerate(s2):
            c1 = s1[k]

            if c1 == c2:
                current += 1
                k += 1
                best = max(best, current)
            else:
                current = 0
                k = i
    return best


def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))

    print(find_LCS_length_iterative("abdca", "cbda"))
    print(find_LCS_length_iterative("passport", "ppsspt"))

    print(find_LCS_length_bottom_up("abdca", "cbda"))
    print(find_LCS_length_bottom_up("passport", "ppsspt"))


main()
