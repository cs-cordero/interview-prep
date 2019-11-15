class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        seen_R = 0
        seen_L = 0
        for s, e in zip(start, end):
            if s == "R":
                seen_R += 1
                seen_L = 0
            elif s == "L":
                seen_L += 1
                seen_R = 0

            if e == "R":
                seen_R -= 1
                seen_L = 0
            elif e == "L":
                seen_L -= 1
                seen_R = 0

            if seen_R < 0:
                return False
            if seen_L > 0:
                return False
        return seen_R == 0 and seen_L == 0
