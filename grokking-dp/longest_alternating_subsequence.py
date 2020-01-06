from typing import List


def find_LAS_length(nums: List[int]) -> int:
    inc = [1] * len(nums)
    dec = [1] * len(nums)

    def find_best_to_increase_from(end: int, increased_to: int) -> int:
        best = -1
        best_value = None
        for i in range(end):
            if nums[i] < increased_to and (best == -1 or dec[i] > best_value):
                best_value = dec[i]
                best = i
        return best

    def find_best_to_decrease_from(end: int, decreased_to: int) -> int:
        best = -1
        best_value = None
        for i in range(end):
            if nums[i] > decreased_to and (best == -1 or inc[i] > best_value):
                best_value = inc[i]
                best = i
        return best

    best = 1
    for i in range(1, len(nums)):
        m = find_best_to_increase_from(i, nums[i])
        n = find_best_to_decrease_from(i, nums[i])
        if m != -1:
            inc[i] = dec[m] + 1
        if n != -1:
            dec[i] = inc[n] + 1
        best = max(inc[i], dec[i])

    print(nums)
    print(inc)
    print(dec)
    return best


def main():
    print(find_LAS_length([1, 2, 3, 4]))
    print(find_LAS_length([3, 2, 1, 4]))
    print(find_LAS_length([1, 3, 2, 4]))


main()
