from collections import deque
from typing import List, Tuple


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return 0

        rows = len(forest)
        cols = len(forest[0])

        def find_path_length(start: Tuple[int, int], end: Tuple[int, int]) -> int:
            queue = deque([(start, 0)])
            visited = {start}
            while queue:
                (row, col), steps = queue.popleft()
                if (row, col) == end:
                    return steps
                for drow, dcol in [
                    (0, -1),
                    (-1, 0),
                    (0, 1),
                    (1, 0),
                ]:
                    next_row = row + drow
                    next_col = col + dcol
                    if (
                        (next_row, next_col) in visited
                        or not (next_row >= 0 and next_row < rows)
                        or not (next_col >= 0 and next_col < cols)
                        or forest[next_row][next_col] == 0
                    ):
                        continue
                    visited.add((next_row, next_col))
                    queue.append(((next_row, next_col), steps + 1))
            return -1

        trees = []
        for row_i, row in enumerate(forest):
            for col_i, value in enumerate(row):
                if value > 1:
                    trees.append((value, (row_i, col_i)))
        trees.sort()

        location = (0, 0)
        steps = 0
        for _, target in trees:
            path_length = find_path_length(location, target)
            if path_length == -1:
                return path_length
            steps += path_length
            location = target
        return steps
