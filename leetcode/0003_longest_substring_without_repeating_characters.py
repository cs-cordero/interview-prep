class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        mid = len(s) // 2
        left = self.lengthOfLongestSubstring(s[:mid])
        right = self.lengthOfLongestSubstring(s[mid:])

        seen = {s[mid]}
        cross = 1
        # expand right
        i = mid + 1
        while i < len(s) and s[i] not in seen:
            seen.add(s[i])
            i += 1
            cross = max(cross, len(seen))
        i -= 1

        # expand left with sliding window
        j = mid - 1
        while j >= 0:
            while s[j] in seen and i > mid and j >= 0:
                seen.remove(s[i])
                i -= 1
            if s[j] in seen:
                break
            seen.add(s[j])
            cross = max(cross, len(seen))
            j -= 1

        return max(cross, left, right)


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
