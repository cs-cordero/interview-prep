from collections import deque
from typing import Iterable, List, Tuple


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        if not image or not image[0]:
            return image
        limits = len(image), len(image[0])

        old_color = image[sr][sc]
        queue = deque([(sr, sc)])
        visited = {(sr, sc)}
        while queue:
            row, col = queue.popleft()
            for nrow, ncol in neighbors(row, col, limits):
                if (nrow, ncol) in visited or image[nrow][ncol] != old_color:
                    continue
                visited.add((nrow, ncol))
                queue.append((nrow, ncol))
            image[row][col] = newColor
        return image


def neighbors(row: int, col: int, limits: Tuple[int, int]) -> Iterable[Tuple[int, int]]:
    if row - 1 >= 0:
        yield row - 1, col
    if col - 1 >= 0:
        yield row, col - 1
    if row + 1 < limits[0]:
        yield row + 1, col
    if col + 1 < limits[1]:
        yield row, col + 1
