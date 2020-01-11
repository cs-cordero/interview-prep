from collections import defaultdict
from typing import List, Optional


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        elif not n or (n > 1 and not edges):
            return False

        graph = defaultdict(list)
        for from_node, to_node in edges:
            graph[from_node].append(to_node)
            graph[to_node].append(from_node)

        visited = set()
        visiting = set()

        def helper(node: int, prev: Optional[int]) -> bool:
            if node in visiting:
                return False

            visiting.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue

                if not helper(neighbor, node):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        return helper(edges[0][0], None) and len(visited) == n
