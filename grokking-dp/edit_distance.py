from collections import defaultdict


def find_min_operations(s1: str, s2: str) -> int:
    memo = defaultdict(lambda: len(s1) + len(s2))

    def helper(i: int, j: int) -> int:
        if i == len(s1):
            return len(s2) - j
        elif j == len(s2):
            return len(s1) - i

        key = (i, j)
        if key not in memo:
            if s1[i] == s2[j]:
                memo[key] = helper(i + 1, j + 1)
            else:
                memo[key] = 1 + min(
                    helper(i + 1, j + 1), helper(i + 1, j), helper(i, j + 1),
                )
        return memo[key]

    return helper(0, 0)


def main():
    print(find_min_operations("bat", "but"))
    print(find_min_operations("abdca", "cbda"))
    print(find_min_operations("passpot", "ppsspqrt"))


main()
