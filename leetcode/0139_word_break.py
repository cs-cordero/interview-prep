from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        queue = deque([0])
        visited = set()
        while queue:
            start = queue.popleft()
            if start in visited:
                continue
            visited.add(start)

            if start == len(s):
                return True
            for end in range(start, len(s)):
                if s[start : end + 1] in words:
                    queue.append(end + 1)
        return False
