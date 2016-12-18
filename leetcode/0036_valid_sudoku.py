from typing import Iterable, List, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return all(
            char == "." or char in get_options(board, (row, col))
            for row, row_data in enumerate(board)
            for col, char in enumerate(row_data)
        )


def get_options(board: List[List[str]], point: Tuple[int, int]) -> Iterable[str]:
    all_options = {str(i) for i in range(1, 10)}

    row, col = point
    same_row = {board[row][_col] for _col in range(9) if _col != col}
    same_col = {board[_row][col] for _row in range(9) if _row != row}
    same_box = {
        board[_row][_col]
        for _row in range((row // 3 * 3), (row // 3 * 3) + 3)
        for _col in range((col // 3 * 3), (col // 3 * 3) + 3)
        if _row != row and _col != col
    }

    for option in all_options - same_row - same_col - same_box:
        yield option


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
board3 = [
    [".", "8", "7", "6", "5", "4", "3", "2", "1"],
    ["2", ".", ".", ".", ".", ".", ".", ".", "."],
    ["3", ".", ".", ".", ".", ".", ".", ".", "."],
    ["4", ".", ".", ".", ".", ".", ".", ".", "."],
    ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    ["6", ".", ".", ".", ".", ".", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    ["8", ".", ".", ".", ".", ".", ".", ".", "."],
    ["9", ".", ".", ".", ".", ".", ".", ".", "."],
]

print(Solution().isValidSudoku(board))
print(Solution().isValidSudoku(board2))
print(Solution().isValidSudoku(board3))
