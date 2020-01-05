def find_LPS_length_brute_force(s: str):
    def helper(start: int, end: int) -> int:
        if start > end:
            return 0
        elif start == end:
            return 1

        if s[start] == s[end]:
            remaining_length = end - start - 1
            if remaining_length == helper(start + 1, end - 1):
                return 2 + remaining_length

        return max(helper(start + 1, end), helper(start, end - 1))

    return helper(0, len(s) - 1)


def main():
    print(find_LPS_length_brute_force("abdbca"))
    print(find_LPS_length_brute_force("cddpd"))
    print(find_LPS_length_brute_force("pqr"))


main()
