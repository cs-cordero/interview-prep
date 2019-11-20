from typing import Iterable, List, Tuple

Point = Tuple[int, int]


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def get_adjacent_points(base_point: Point) -> Iterable[Point]:
            x, y = base_point
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    if x + dx >= 0 and y + dy >= 0 and x + dx < rows and y + dy < cols:
                        yield (x + dx, y + dy)

        # 2 == Live
        # 3 == Birth
        # 4 == Die

        def mark_with_transition() -> None:
            for row_i, row in enumerate(board):
                for col_i, value in enumerate(row):
                    live_neighbors = 0
                    for nrow, ncol in get_adjacent_points((row_i, col_i)):
                        if board[nrow][ncol] in (1, 2, 4):
                            live_neighbors += 1
                    if value == 1:
                        if live_neighbors < 2:
                            board[row_i][col_i] = 4
                        elif live_neighbors < 4:
                            board[row_i][col_i] = 2
                        else:
                            board[row_i][col_i] = 4
                    elif live_neighbors == 3:
                        board[row_i][col_i] = 3

        def perform_transition() -> None:
            for row_i, row in enumerate(board):
                for col_i, value in enumerate(row):
                    if value == 2:
                        board[row_i][col_i] = 1
                    elif value == 3:
                        board[row_i][col_i] = 1
                    elif value == 4:
                        board[row_i][col_i] = 0

        mark_with_transition()
        perform_transition()
