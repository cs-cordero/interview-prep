def find_SPM_count(s: str, p: str) -> int:
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
    for j in range(len(s) + 1):
        dp[0][j] = 1

    for i, p_char in enumerate(p, 1):
        for j, s_char in enumerate(s, 1):
            dp[i][j] = dp[i][j - 1]
            if p_char == s_char:
                dp[i][j] += dp[i - 1][j - 1]

    return dp[-1][-1]


def main():
    print(find_SPM_count("baxmx", "ax"))
    print(find_SPM_count("tomorrow", "tor"))


main()

"""
  - t o m o r r o w
- 0 0 0 0 0 0 0 0 0
t 0 1 1 1 1 1 1 1 1
o 0   1 1 2 2 2 3 3
r 0         2 4 4 4

  t o m o r r o w -
t 4 0 0 0 0 0 0 0 0
o 4 4 3 3 1 1 1 0 0
r 2 2 2 2 2 1 0 0 0
- 1 1 1 1 1 1 1 1 1

c1 = find_SPM_count_recursive(str, pat, strIndex + 1, patIndex + 1)
c2 = find_SPM_count_recursive(str, pat, strIndex + 1, patIndex)
return c1 + c2
"""
