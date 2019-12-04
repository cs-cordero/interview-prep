class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        slow = 0
        result = 0
        for fast, character in enumerate(s):
            while character in seen:
                seen.remove(s[slow])
                slow += 1

            seen.add(character)
            result = max(result, fast - slow + 1)
        return result
