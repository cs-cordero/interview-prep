def count_trees(n: int) -> int:
    def helper(n: int) -> int:
        if n <= 1:
            return 1

        count = 0
        for i in range(n):
            count += helper(i - 0) * helper(n - i - 1)
        return count

    if n < 1:
        return 0
    return helper(n)


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
