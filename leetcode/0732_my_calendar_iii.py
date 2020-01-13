from collections import Counter


class MyCalendarThree:
    def __init__(self):
        self.deltas = Counter()

    def book(self, start: int, end: int) -> int:
        self.deltas[start] += 1
        self.deltas[end] -= 1

        result = 0
        current = 0
        for time in sorted(self.deltas):
            current += self.deltas[time]
            result = max(result, current)
        return result
