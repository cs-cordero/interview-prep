class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        return sum(stone in jewels for stone in S)
