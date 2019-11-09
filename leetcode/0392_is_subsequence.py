class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0
        pointer_t = 0
        while pointer_s < len(s):
            char_s = s[pointer_s]
            while pointer_t < len(t):
                if char_s == t[pointer_t]:
                    break
                pointer_t += 1

            if pointer_t >= len(t):
                return False

            if char_s == t[pointer_t]:
                pointer_s += 1
                pointer_t += 1

        return True


print(Solution().isSubsequence("abc", "ahbgdc"))
