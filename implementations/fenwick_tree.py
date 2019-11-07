from typing import List


class FenwickTree:
    def __init__(self, array: List[int]) -> None:
        self._data = [0] + array[:]
        for i, value in enumerate(self._data):
            j = i + get_least_significant_bit_value(i)
            if j < len(self._data):
                self._data[j] += value

    def prefix_sum(self, index: int) -> int:
        result = 0
        while index > 0:
            result += self._data[index]
            index -= get_least_significant_bit_value(index)
        return result

    def sum_range(self, i: int, j: int) -> int:
        """ indexes are assumed to be 0-based, like the input array """
        return self.prefix_sum(j + 1) - self.prefix_sum(i)

    def add_to_index(self, i: int, x: int) -> None:
        """ indexes are assumed to be 0-based, like the input array """
        i += 1
        while i < len(self._data):
            self._data[i] += x
            i += get_least_signifiant_bit_value(i)


def get_least_significant_bit_value(value: int) -> int:
    return value & -value


tree = FenwickTree([3, 4, -2, 7, 3, 11, 5, -8, -9, 2, 4, -8])
assert tree._data == [0, 3, 7, -2, 12, 3, 14, 5, 23, -9, -7, 4, -11]
assert tree.sum_range(2, 6) == -2 + 7 + 3 + 11 + 5
