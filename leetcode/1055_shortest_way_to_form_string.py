class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_i = 0
        target_i = 0
        result = 0
        source_chars = set(source)

        while target_i < len(target):
            if target[target_i] not in source_chars:
                return -1

            if target[target_i] == source[source_i]:
                target_i += 1

            source_i += 1
            if source_i == len(source):
                source_i %= len(source)
                result += 1

        if source_i > 0:
            result += 1

        return result


print(Solution().shortestWay("abc", "abcbc"))
print(Solution().shortestWay("abc", "acdbc"))
print(Solution().shortestWay("xyz", "xzyxz"))
print(Solution().shortestWay("aaaaa", "aaaaaaaaaaaaa"))
