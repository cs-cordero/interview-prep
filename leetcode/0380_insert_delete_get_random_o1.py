import random


class RandomizedSet:
    def __init__(self):
        self.mapping = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.mapping:
            return False

        self.mapping[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapping:
            return False

        val_at_end = self.array[-1]

        index = self.mapping[val]
        self.array[index], self.array[-1] = self.array[-1], self.array[index]
        self.array.pop()
        del self.mapping[val]
        if val_at_end != val:
            self.mapping[val_at_end] = index
        return True

    def getRandom(self) -> int:
        return self.array[random.randint(0, len(self.array) - 1)]
