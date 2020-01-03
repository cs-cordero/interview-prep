from collections import defaultdict
from heapq import heappop, heappush
from typing import Iterable, Tuple


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        visited = defaultdict(lambda: float("inf"))
        pq = []
        heappush(
            pq, (0, get_distance(0, 0, x, y), 0, 0),
        )
        min_dist_so_far = float("inf")
        while pq:
            steps, dist, row, col = heappop(pq)
            if steps >= visited[(row, col)]:
                continue
            if row == x and col == y:
                return steps
            if dist > min_dist_so_far and dist > 4:
                continue
            min_dist_so_far = min(min_dist_so_far, dist)

            visited[(row, col)] = steps
            for next_row, next_col in get_knight_moves(row, col):
                next_dist = get_distance(next_row, next_col, x, y)
                if next_dist > dist and next_dist > 4:
                    # we are getting farther from the target
                    # and we aren't in range to just remanuever
                    continue
                heappush(pq, (steps + 1, next_dist, next_row, next_col))
        assert False, "Invariant"


KNIGHT_DELTAS = [
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
]


def get_knight_moves(row: int, col: int) -> Iterable[Tuple[int, int]]:
    for drow, dcol in KNIGHT_DELTAS:
        yield row + drow, col + dcol


def get_distance(r1: int, c1: int, r2: int, c2: int) -> int:
    return abs(r2 - r1) + abs(c2 - c1)
