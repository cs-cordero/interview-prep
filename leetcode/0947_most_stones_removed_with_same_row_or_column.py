from collections import deque
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = set()

        points_by_row = {}
        points_by_col = {}
        for stone in stones:
            points_by_row.setdefault(stone[0], set()).add(tuple(stone))
            points_by_col.setdefault(stone[1], set()).add(tuple(stone))

        move_count = 0
        for row, col in stones:
            stone = (row, col)
            if stone in visited:
                continue
            visited.add(stone)

            queue = deque([stone])
            size = 1
            while queue:
                current_row, current_col = queue.popleft()
                other_stones = (
                    points_by_row[current_row] | points_by_col[current_col]
                ) - visited
                for other_stone in other_stones:
                    visited.add(other_stone)
                    queue.append(other_stone)
                    size += 1
            move_count += size - 1
        return move_count


print(Solution().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
print(Solution().removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
print(Solution().removeStones([[0, 0]]))
