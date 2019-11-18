from bisect import bisect
from random import randint
from typing import List


class Solution:
    def __init__(self, w: List[int]) -> None:
        self.weights = w
        self.indexes = [0]
        for weight in self.weights:
            self.indexes.append(weight + self.indexes[-1])

    def pickIndex(self) -> int:
        random_index = randint(0, self.indexes[-1] - 1)
        return bisect(self.indexes, random_index) - 1
