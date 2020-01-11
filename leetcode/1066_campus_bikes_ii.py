from collections import defaultdict
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Dict, List


@dataclass
class Edge:
    dist: int
    flow: int
    max_flow: int

    @property
    def capacity(self) -> int:
        return self.max_flow - self.flow


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        graph = create_graph(workers, bikes)

        def is_worker(index: str) -> bool:
            return index not in ("SOURCE", "SINK") and int(index) < len(workers)

        def is_bike(index: str) -> bool:
            return index not in ("SOURCE", "SINK") and int(index) >= len(workers)

        assignments = [None for _ in range(len(workers))]

        while True:
            max_flow_path = find_path(graph)
            if not max_flow_path:
                break

            prev, *path = max_flow_path
            for next_node in path:
                graph[prev][next_node].flow += 1
                graph[next_node][prev].flow -= 1
                if is_worker(prev) and is_bike(next_node):
                    assignments[int(prev)] = int(next_node) - len(workers)
                prev = next_node

        return sum(
            graph[str(worker)][str(bike + len(workers))].dist
            for worker, bike in enumerate(assignments)
        )


def create_graph(
    workers: List[List[int]], bikes: List[List[int]]
) -> Dict[str, Dict[str, Edge]]:
    graph = defaultdict(dict)
    for worker_index, worker in enumerate(workers):
        worker_name = str(worker_index)
        graph["SOURCE"][worker_name] = Edge(dist=0, flow=0, max_flow=1)
        graph[worker_name]["SOURCE"] = Edge(dist=0, flow=0, max_flow=0)

        for bike_index, bike in enumerate(bikes):
            wx, wy = worker
            bx, by = bike
            dist = abs(wy - by) + abs(wx - bx)

            bike_name = str(bike_index + len(workers))
            graph[worker_name][bike_name] = Edge(dist=dist, flow=0, max_flow=1)
            graph[bike_name][worker_name] = Edge(dist=-dist, flow=0, max_flow=0)

            if "SINK" not in graph[bike_name]:
                graph[bike_name]["SINK"] = Edge(dist=0, flow=0, max_flow=1)
                graph["SINK"][bike_name] = Edge(dist=0, flow=0, max_flow=0)

    return graph


def find_path(graph: Dict[str, Dict[str, Edge]]) -> List[str]:
    heap = [(0, ["SOURCE"])]
    while heap:
        current_dist, current_path = heappop(heap)
        current_node = current_path[-1]
        if current_node == "SINK":
            return current_path

        for neighbor, edge in graph[current_node].items():
            if edge.capacity == 0 or neighbor in current_path:
                continue
            key = (current_dist + edge.dist, current_path + [neighbor])
            heappush(heap, key)
    return []


print(Solution().assignBikes([[0, 0], [0, 2]], [[0, 1], [0, 7]]))  # 6
print(Solution().assignBikes([[0, 0], [2, 1]], [[1, 2], [3, 3]]))  # 6
