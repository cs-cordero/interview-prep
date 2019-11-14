from typing import Tuple


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        restrictions = {
            (1, 3): 2,
            (3, 1): 2,
            (1, 9): 5,
            (9, 1): 5,
            (1, 7): 4,
            (7, 1): 4,
            (9, 7): 8,
            (7, 9): 8,
            (9, 3): 6,
            (3, 9): 6,
            (3, 7): 5,
            (7, 3): 5,
            (4, 6): 5,
            (6, 4): 5,
            (2, 8): 5,
            (8, 2): 5,
        }
        paths = set()

        def dfs(current: int, visited: Tuple[int, ...], k: int) -> None:
            if k >= m:
                paths.add(visited)
            if k >= n:
                return None

            for target in range(1, 10):
                if target in visited:
                    continue
                required_to_reach_target = restrictions.get((current, target))
                if required_to_reach_target and required_to_reach_target not in visited:
                    continue

                next_visited = tuple([*visited, target])
                dfs(target, next_visited, k + 1)

        for start in range(1, 10):
            dfs(start, (start,), 1)
        return len(paths)
