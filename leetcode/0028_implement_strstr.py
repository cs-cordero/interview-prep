class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif len(needle) > len(haystack):
            return -1

        target_hash = 0
        for i, character in enumerate(needle):
            target_hash += ord(character) << (8 * i)

        current_hash = 0
        for i in range(len(needle)):
            current_hash += ord(haystack[i]) << (8 * i)

        if current_hash == target_hash:
            return 0

        for i in range(len(needle), len(haystack)):
            current_hash >>= 8
            current_hash |= ord(haystack[i]) << (8 * (len(needle) - 1))
            if current_hash == target_hash:
                return i - len(needle) + 1
        return -1
