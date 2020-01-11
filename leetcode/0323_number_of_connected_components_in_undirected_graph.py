from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.components = list(range(n))
        self.count = n

    def union(self, a: int, b: int) -> None:
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            self.components[parent_a] = parent_b
            self.count -= 1

    def find(self, i: int) -> int:
        if self.components[i] != i:
            self.components[i] = self.find(self.components[i])
        return self.components[i]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.count
