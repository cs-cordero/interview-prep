from collections import defaultdict


class TimeMap:
    def __init__(self) -> None:
        self._dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self._dict.get(key)
        if not entries:
            return ""
        left = 0
        right = len(entries) - 1
        while left < right:
            mid = (left + right) // 2
            if entries[mid][0] < timestamp:
                left = mid + 1
            elif entries[mid][0] > timestamp:
                right = mid - 1
            else:
                return entries[mid][1]

        actual = left - 1 if timestamp < entries[left][0] else left
        return entries[actual][1] if actual >= 0 else ""
