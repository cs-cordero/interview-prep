from collections import defaultdict
from heapq import heappop, heappush
from typing import List, NamedTuple


class Edge(NamedTuple):
    from_node: str
    to_node: str
    distance: int


def dijkstra(edges: List[Edge], source: str):
    # transform edges into a dict representation so we can get neighbors easily
    graph = defaultdict(list)
    for edge in edges:
        graph[edge.from_node].append(edge)

    # initialize our results
    distances = defaultdict(lambda: float("inf"))
    paths = {}

    # initialize heap
    heap = [(0, source, [source])]

    while heap:
        current_dist, current_node, current_path = heappop(heap)
        if current_dist >= distances[current_node]:
            continue

        distances[current_node] = current_dist
        paths[current_node] = current_path

        for edge in graph[current_node]:
            cost_to_reach_target = current_dist + edge.distance
            if cost_to_reach_target < distances[edge.to_node]:
                heap_entry = (
                    cost_to_reach_target,
                    edge.to_node,
                    current_path + [edge.to_node],
                )
                heappush(heap, heap_entry)

    return distances, paths


"""
Example:

a -> b (costs 10)
a -> c (costs 5)
b -> d (costs 4)
b -> e (costs 3)
c -> d (costs 6)

a - b - e
 \ / \
  c - d
"""  # noqa

edges = [
    Edge("a", "b", 10),
    Edge("a", "c", 5),
    Edge("b", "d", 4),
    Edge("b", "e", 3),
    Edge("c", "b", 1),
    Edge("c", "d", 6),
]
distances, paths = dijkstra(edges, "a")

print(paths["d"])  # shortest path from a to d
print(paths["e"])  # shortest path from a to e
