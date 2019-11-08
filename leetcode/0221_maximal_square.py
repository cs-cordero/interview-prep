from typing import List, Set, Tuple


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        limits = len(matrix), len(matrix[0])

        def get_next_coordinates_for_square(
            current_coordinates: Set[Tuple[int, int]]
        ) -> Set[Tuple[int, int]]:
            next_coordinates = set()
            for coordinate in current_coordinates:
                row, col = coordinate
                if row + 1 >= limits[0] or col + 1 >= limits[1]:
                    # The square can't get any bigger.  No coordinate is valid.
                    next_coordinates.clear()
                    return next_coordinates

                candidates = [(row + 1, col), (row, col + 1), (row + 1, col + 1)]
                for candidate in candidates:
                    if candidate not in current_coordinates:
                        next_coordinates.add(candidate)
            return next_coordinates

        def all_coordinates_valid(coordinates: Set[Tuple[int, int]]) -> bool:
            return all(matrix[row][col] == "1" for row, col in coordinates)

        def mark_coordinates_visited(coordinates: Set[Tuple[int, int]]) -> None:
            for row, col in coordinates:
                matrix[row][col] = "0"

        result = 0
        for row_i, row in enumerate(matrix):
            for col_i, col in enumerate(row):
                if col == "0":
                    continue

                size = 1
                matrix[row_i][col_i] = 0
                coordinates = {(row_i, col_i)}
                while True:
                    coordinates = get_next_coordinates_for_square(coordinates)
                    if not coordinates or not all_coordinates_valid(coordinates):
                        break
                    size += 1
                size **= 2
                result = max(result, size)
        return result


foo = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(Solution().maximalSquare(foo))

bar = [
    ["0", "0", "0", "1"],
    ["1", "1", "0", "1"],
    ["1", "1", "1", "1"],
    ["0", "1", "1", "1"],
    ["0", "1", "1", "1"],
]
print(Solution().maximalSquare(bar))
