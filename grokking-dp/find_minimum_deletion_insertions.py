def find_MDI(s1: str, s2: str) -> None:
    def helper(i: int, j: int, operations: int) -> int:
        if i == len(s1):
            return operations + len(s2) - j
        elif j == len(s2):
            return operations + len(s1) - i

        if s1[i] == s2[j]:
            return helper(i + 1, j + 1, operations)
        else:
            return min(
                helper(i + 1, j, operations + 1), helper(i, j + 1, operations + 1),
            )

    c1 = helper(0, 0, 0)
    print(f"{c1=}")
    print("Minimum deletions needed: " + str(len(s1) - c1))
    print("Minimum insertions needed: " + str(len(s2) - c1))


def main():
    find_MDI("abc", "abc")
    find_MDI("abc", "fbc")
    find_MDI("abdca", "cbda")
    find_MDI("passport", "ppsspt")


main()
