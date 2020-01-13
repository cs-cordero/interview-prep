from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.uf = list(range(n))
        self.components = n

    def find(self, i: int) -> int:
        if self.uf[i] != i:
            self.uf[i] = self.find(self.uf[i])
        return self.uf[i]

    def union(self, a: int, b: int) -> None:
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            self.uf[parent_a] = parent_b
            self.components -= 1


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind(len(M))
        for i in range(len(M)):
            row = M[i]
            for j in range(i + 1, len(row)):
                value = row[j]
                if value == 1:
                    uf.union(i, j)
        return uf.components
