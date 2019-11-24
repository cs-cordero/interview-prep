from collections import defaultdict
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False for _ in range(n)]
        visiting = [False for _ in range(n)]

        graph = defaultdict(set)
        for source, target in edges:
            graph[source].add(target)
            graph[target].add(source)

        def dfs(node: int, prev: int) -> bool:
            if visiting[node]:
                return False
            visiting[node] = True

            for neighbor in graph[node]:
                if visited[node] or neighbor == prev:
                    continue

                if dfs(neighbor, node) is False:
                    return False

            visiting[node] = False
            visited[node] = True
            return True

        if not dfs(0, 0):
            return False
        return all(visited)
