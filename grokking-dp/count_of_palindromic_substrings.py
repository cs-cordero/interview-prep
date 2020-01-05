def count_PS(s: str) -> int:
    memo = {}
    count = 0

    def helper(start: int, end: int) -> bool:
        nonlocal count

        key = (start, end)
        if key in memo:
            return memo[key]

        if start > end:
            return True
        elif start == end:
            memo[key] = True
            count += 1
            return memo[key]
        elif s[start] == s[end]:
            if helper(start + 1, end - 1):
                memo[key] = True
                count += 1
            else:
                memo[key] = False
        elif s[start] != s[end]:
            memo[key] = False

        helper(start + 1, end)
        helper(start, end - 1)

        return memo[key]

    helper(0, len(s) - 1)
    return count


def main():
    print(count_PS("abdbca"))
    print(count_PS("cddpd"))
    print(count_PS("pqr"))
    print(count_PS("qqq"))


main()
