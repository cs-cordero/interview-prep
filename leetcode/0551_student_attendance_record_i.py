class Solution:
    def checkRecord(self, s: str) -> bool:
        seen_a = False
        for i, character in enumerate(s):
            if character == "A":
                if seen_a:
                    return False
                seen_a = True
            elif character == "L":
                if i + 2 < len(s) and s[i + 1] == "L" and s[i + 2] == "L":
                    return False
        return True
