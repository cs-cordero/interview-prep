def find_minimum_deletions(s: str) -> int:
    memo = {}

    def helper(start: int, end: int) -> int:
        key = (start, end)
        if key not in memo:
            if start > end:
                memo[key] = 0
            elif s[start] == s[end]:
                memo[key] = helper(start + 1, end - 1)
            else:
                skip_left = helper(start + 1, end)
                skip_right = helper(start, end - 1)
                memo[key] = 1 + min(skip_left, skip_right)
        return memo[key]

    return helper(0, len(s) - 1)


def main():
    print(find_minimum_deletions("abdbca"))
    print(find_minimum_deletions("cddpd"))
    print(find_minimum_deletions("pqr"))


main()
