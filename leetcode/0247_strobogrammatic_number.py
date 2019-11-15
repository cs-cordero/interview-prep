class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo_map = {"1": "1", "6": "9", "8": "8", "9": "6", "0": "0"}

        if not num or (len(num) > 1 and num[-1] == "0"):
            return False

        left = 0
        right = len(num) - 1
        while left <= right:
            expected = strobo_map.get(num[left])
            if expected is None or expected != num[right]:
                return False
            left += 1
            right -= 1
        return True
