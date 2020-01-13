from collections import defaultdict
from typing import List, Set


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        result = []
        if not connections:
            return result

        graph = defaultdict(list)
        for from_server, to_server in connections:
            graph[from_server].append(to_server)
            graph[to_server].append(from_server)

        visited = set()
        visiting = set()

        def helper(node: int, prev: int) -> Set[int]:
            cycles = set()
            if node in visiting:
                cycles.add(node)
                return cycles

            visiting.add(node)
            for neighbor in graph[node]:
                if neighbor in visited or neighbor == prev:
                    continue

                downstream_cycles = helper(neighbor, node)
                if not downstream_cycles:
                    result.append([node, neighbor])
                cycles |= downstream_cycles

            visited.add(node)
            visiting.remove(node)
            if node in cycles:
                cycles.remove(node)
            return cycles

        for node in range(n):
            if node in visited:
                continue
            helper(node, -1)
        return result
