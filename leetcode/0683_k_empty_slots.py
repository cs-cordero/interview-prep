from bisect import bisect_left
from typing import List


class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        sorted_arr = []
        for day, bulb in enumerate(bulbs):
            bipoint = bisect_left(sorted_arr, bulb)
            sorted_arr.insert(bipoint, bulb)
            if (bipoint - 1 >= 0 and bulb - sorted_arr[bipoint - 1] - 1 == K) or (
                bipoint + 1 < len(sorted_arr)
                and sorted_arr[bipoint + 1] - bulb - 1 == K
            ):
                return day + 1
        return -1
