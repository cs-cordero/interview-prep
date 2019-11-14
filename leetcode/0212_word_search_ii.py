from typing import Iterable, List, Set, Tuple

Point = Tuple[int, int]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        all_words = set()
        prefixes = set()
        for word in words:
            all_words.add(word)
            for i in range(1, len(word) + 1):
                prefixes.add(word[:i])

        def dfs(string: str, point: Point, visited: Set[Point]) -> Set[str]:
            result = set()
            if string not in prefixes:
                return result
            if string in all_words:
                result.add(string)

            next_visited = {*visited, point}
            for next_point in next_points(point, next_visited):
                row, col = next_point
                result |= dfs(f"{string}{board[row][col]}", next_point, next_visited)
            return result

        def next_points(point: Point, visited: Set[Point]) -> Iterable[Point]:
            row, col = point
            for x, y in (
                (row - 1, col),
                (row, col - 1),
                (row + 1, col),
                (row, col + 1),
            ):
                if (
                    x < 0
                    or y < 0
                    or x >= len(board)
                    or y >= len(board[0])
                    or (x, y) in visited
                ):
                    continue
                yield x, y

        answer = set()
        for row_i, row in enumerate(board):
            for col_i, col in enumerate(row):
                answer |= dfs(col, (row_i, col_i), set())
        return list(answer)
