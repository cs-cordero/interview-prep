from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.uf = list(range(n))
        self.lengths = [1] * n
        self.components = n

    def find(self, i: int) -> int:
        if i != self.uf[i]:
            self.uf[i] = self.find(self.uf[i])
        return self.uf[i]

    def union(self, i: int, j: int) -> None:
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return None
        self.uf[parent_i] = parent_j
        self.lengths[parent_j] += self.lengths[parent_i]
        self.lengths[parent_i] = 0


def journeyToMoon(n: int, astronaut: List[List[int]]):
    uf = UnionFind(n)
    for astronaut1, astronaut2 in astronaut:
        uf.union(astronaut1, astronaut2)

    countries = [count for count in uf.lengths if count > 0]

    if len(countries) <= 1:
        return 0

    answer = 0
    count = countries[0]
    for i in range(1, len(countries)):
        answer += count * countries[i]
        count += countries[i]
    return answer
