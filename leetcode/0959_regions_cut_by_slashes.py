from collections import deque
from dataclasses import dataclass
from typing import Iterable, List, Optional, Tuple


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid:
            return 0

        limit = len(grid), len(grid[0])
        graph = {}
        for row, _row in enumerate(grid):
            for col, value in enumerate(_row):
                if value == " ":
                    node = Node(row, col, value, None, limit)
                    graph[(row, col)] = (node, node)
                elif value in ("/", "\\"):
                    graph[(row, col)] = (
                        Node(row, col, value, False, limit),
                        Node(row, col, value, True, limit),
                    )
                else:
                    assert False, "Invariant"

        regions = 0
        visited = set()
        for coordinate, nodes in graph.items():
            for node in nodes:
                if node in visited:
                    continue
                queue = deque([node])
                seen_this_round = []
                while queue:
                    current = queue.popleft()
                    if current in visited:
                        continue
                    visited.add(current)
                    seen_this_round.append(current)
                    for point in current.reachable_points:
                        reachable_nodes = graph[point]
                        node_type = reachable_nodes[0].slash_type
                        row, col = point
                        if row < current.row:
                            # going up
                            if node_type == "/":
                                target_node = reachable_nodes[1]
                            else:
                                target_node = reachable_nodes[0]
                        elif row > current.row:
                            # going down
                            if node_type == "/":
                                target_node = reachable_nodes[0]
                            else:
                                target_node = reachable_nodes[1]
                        elif col > current.col:
                            # going right
                            if node_type == "/":
                                target_node = reachable_nodes[0]
                            else:
                                target_node = reachable_nodes[0]
                        elif col < current.col:
                            # going left
                            if node_type == "/":
                                target_node = reachable_nodes[1]
                            else:
                                target_node = reachable_nodes[1]
                        queue.append(target_node)
                regions += 1
        return regions


@dataclass(unsafe_hash=True)
class Node:
    row: int
    col: int
    slash_type: str
    orientation: Optional[bool]
    graph_limit: Tuple[int, int]

    @property
    def reachable_points(self) -> Iterable[Tuple[int, int]]:
        up = (self.row - 1, self.col) if self.row - 1 >= 0 else None
        left = (self.row, self.col - 1) if self.col - 1 >= 0 else None
        down = (self.row + 1, self.col) if self.row + 1 < self.graph_limit[0] else None
        right = (self.row, self.col + 1) if self.col + 1 < self.graph_limit[1] else None

        if self.slash_type == " ":
            directions = [up, left, down, right]
        elif self.slash_type == "/":
            if self.orientation is False:
                directions = [up, left]
            elif self.orientation is True:
                directions = [down, right]
        elif self.slash_type == "\\":
            if self.orientation is False:
                directions = [left, down]
            elif self.orientation is True:
                directions = [right, up]
        for direction in directions:
            if direction is not None:
                yield direction


print(Solution().regionsBySlashes(["\\/", "/\\"]))
