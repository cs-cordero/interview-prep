from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for a, b in zip_longest(
            map(int, version1.split(".")), map(int, version2.split(".")), fillvalue=0
        ):
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
