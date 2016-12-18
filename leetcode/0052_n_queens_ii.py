from typing import Iterable, Set, Tuple


class Queen:
    def __init__(self, position: Tuple[int, int], board_size: int) -> None:
        self.position = position
        self.board_size = board_size

    @property
    def attacked_positions(self) -> Iterable[Tuple[int, int]]:
        x, y = self.position
        for col in range(self.board_size):
            yield (x, col)

        for row in range(self.board_size):
            if (row, y) == (x, y):
                continue
            yield (row, y)

        for direction in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            dx, dy = direction
            r, c = x + dx, y + dy
            while r >= 0 and c >= 0 and r < self.board_size and c < self.board_size:
                yield (r, c)
                r += dx
                c += dy


def is_valid(row: int, board_size: int, seen_positions: Set[Tuple[int, int]]) -> int:
    if row >= board_size:
        # base case, board was valid
        return 1

    count = 0
    for col in range(board_size):
        if (row, col) in seen_positions:
            continue

        next_queen = Queen((row, col), board_size)
        next_positions = seen_positions | set(next_queen.attacked_positions)
        count += is_valid(row + 1, board_size, next_positions)
    return count


class Solution:
    def totalNQueens(self, n: int) -> int:
        return is_valid(row=0, board_size=n, seen_positions=set())


print(Solution().totalNQueens(8))
