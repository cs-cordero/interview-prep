from copy import copy
from typing import Optional, Set


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def helper(current: str, visited: Set[str]) -> Optional[str]:
            if len(current) >= n:
                last_n = current[-n:]
                if last_n in visited:
                    return None
                visited.add(last_n)
                if len(visited) == n ** k:
                    return current

            for value in range(k):
                result = helper(f"{current}{value}", copy(visited))
                if result is not None:
                    return result

            return None

        return helper("", set())
