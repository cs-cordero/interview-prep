from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not s:
            return ""

        t_counts = Counter(t)
        s_counts = Counter(s[: len(t)])

        def check() -> bool:
            for k, v in t_counts.items():
                if s_counts.get(k, 0) < v:
                    return False
            return True

        result = None if not check() else s[: len(t)]
        begin = 0
        for end in range(len(t), len(s)):
            s_counts[s[end]] += 1
            while check():
                candidate = s[begin : end + 1]
                if result is None or len(candidate) < len(result):
                    result = candidate
                s_counts[s[begin]] -= 1
                begin += 1
        return result or ""


print(Solution().minWindow("ADOBECODEBANC", "ABCC"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a", "a"))
