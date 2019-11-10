from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        current = defaultdict(int)
        required = defaultdict(int)
        for char in t:
            required[char] += 1

        best = None
        while left <= right and right < len(s):
            current[s[right]] += 1
            while left <= right and all(
                amount <= current.get(c, 0) for c, amount in required.items()
            ):
                # All characters accounted for
                candidate = s[left : right + 1]
                if best is None or len(candidate) < len(best):
                    best = candidate

                leftmost_char = s[left]
                current[leftmost_char] -= 1
                left += 1
            right += 1
        return best or ""
