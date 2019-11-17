from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class Edge:
    source: int
    target: int
    cost: int
    flow: int = 0
    capacity: int = 1
    residual: Optional["Edge"] = None

    @property
    def remaining_capacity(self) -> int:
        return self.capacity - self.flow

    @classmethod
    def create_pair(
        cls, source: int, target: int, cost: int, flow: int = 0, capacity: int = 1
    ) -> Tuple["Edge", "Edge"]:
        primary = Edge(
            source=source, target=target, cost=cost, flow=flow, capacity=capacity
        )
        residual = Edge(
            source=target,
            target=source,
            cost=-cost,
            flow=-flow,
            capacity=0,
            residual=primary,
        )
        primary.residual = residual
        return primary, residual


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        edges = setup_edge_list(workers, bikes)
        vertices = len(workers) + len(bikes) + 2
        source_i = vertices - 2
        target_i = vertices - 1
        assignments = {}
        cost = 0

        def is_worker(i: int) -> bool:
            return i < len(workers)

        def is_bike(i: int) -> bool:
            return i < (len(workers) + len(bikes)) and not is_worker(i)

        def bellman_ford() -> Tuple[List[int], List[int]]:
            distances = [float("inf") for _ in range(vertices)]
            distances[source_i] = 0
            prev_vertices = [None for _ in range(vertices)]
            prev_edges = [None for _ in range(vertices)]
            for _ in range(vertices - 1):
                for edge_i, edge in enumerate(edges):
                    if edge.remaining_capacity <= 0:
                        continue
                    if distances[edge.target] > distances[edge.source] + edge.cost:
                        distances[edge.target] = distances[edge.source] + edge.cost
                        prev_vertices[edge.target] = edge.source
                        prev_edges[edge.target] = edge_i
            return prev_vertices, prev_edges

        def update_flow_along_path(
            reversed_vertex_path: List[int], reversed_edge_path: List[int]
        ) -> Tuple[Dict[int, int], int]:
            worker_to_bike_assignments = {}
            delta_cost = 0
            vertex = target_i
            while vertex != source_i:
                edge = edges[reversed_edge_path[vertex]]
                edge.flow += 1
                edge.residual.flow -= 1
                if is_bike(edge.target) and is_worker(edge.source):
                    worker_to_bike_assignments[edge.source] = edge.target
                delta_cost += edge.cost
                vertex = reversed_vertex_path[vertex]
            return worker_to_bike_assignments, delta_cost

        while len(assignments) < len(workers):
            new_assignments, delta_cost = update_flow_along_path(*bellman_ford())
            assignments.update(new_assignments)
            cost += delta_cost
        return cost


def setup_edge_list(workers: List[List[int]], bikes: List[List[int]]) -> int:
    edges = []
    for worker_i, (worker_x, worker_y) in enumerate(workers):
        for bike_i, (bike_x, bike_y) in enumerate(bikes):
            distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)
            edges.extend(Edge.create_pair(worker_i, bike_i + len(workers), distance))

    source_i = len(workers) + len(bikes)
    target_i = source_i + 1
    for worker_i in range(len(workers)):
        edges.extend(Edge.create_pair(source_i, worker_i, 0))
    for bike_i in range(len(bikes)):
        edges.extend(Edge.create_pair(bike_i + len(workers), target_i, 0))
    return edges


print(Solution().assignBikes([[0, 0], [0, 2]], [[0, 1], [0, 7]]))  # 6
print(Solution().assignBikes([[0, 0], [2, 1]], [[1, 2], [3, 3]]))  # 6
