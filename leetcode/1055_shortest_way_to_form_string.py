class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if set(target) - set(source):
            return -1

        target_i = 0
        subsequences = 0
        while target_i < len(target):
            for char in source:
                if char == target[target_i]:
                    target_i += 1
                if target_i >= len(target):
                    break
            subsequences += 1
        return subsequences
