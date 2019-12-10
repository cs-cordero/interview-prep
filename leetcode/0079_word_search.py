from typing import Iterable, List, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        elif not board or not board[0]:
            return False

        visiting = set()
        limits = len(board), len(board[0])

        def dfs_helper(current: Tuple[int, int], i: int) -> bool:
            if board[current[0]][current[1]] != word[i]:
                return False
            if i == len(word) - 1:
                return True

            visiting.add(current)

            for neighbor in neighbors(current, limits):
                if neighbor in visiting:
                    continue
                if dfs_helper(neighbor, i + 1):
                    return True

            visiting.remove(current)
            return False

        for row_i, row in enumerate(board):
            for col_i, value in enumerate(row):
                if dfs_helper((row_i, col_i), 0):
                    return True
        return False


def neighbors(
    point: Tuple[int, int], limits: Tuple[int, int]
) -> Iterable[Tuple[int, int]]:
    row, col = point
    if row - 1 >= 0:
        yield row - 1, col
    if col - 1 >= 0:
        yield row, col - 1
    if row + 1 < limits[0]:
        yield row + 1, col
    if col + 1 < limits[1]:
        yield row, col + 1
