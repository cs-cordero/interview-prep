from collections import deque
from typing import Iterable, List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends or target in deadends:
            return -1

        queue = deque([("0000", 0)])
        deadends.add("0000")
        while queue:
            current, steps = queue.popleft()
            if current == target:
                return steps

            for move in moves(current):
                if move in deadends:
                    continue
                deadends.add(move)
                queue.append((move, steps + 1))
        return -1


def moves(base: str) -> Iterable[str]:
    for i, val in enumerate(base):
        num = int(val)
        yield f"{base[:i]}{(num+1)%10}{base[i+1:]}"
        yield f"{base[:i]}{(num-1)%10}{base[i+1:]}"
