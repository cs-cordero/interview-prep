from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.stacks_by_freq = defaultdict(list)
        self.freqs = defaultdict(int)
        self.highest_freq = 0

    def push(self, x: int) -> None:
        self.freqs[x] += 1
        self.stacks_by_freq[self.freqs[x]].append(x)
        self.highest_freq = max(self.highest_freq, self.freqs[x])

    def pop(self) -> int:
        value = self.stacks_by_freq[self.highest_freq].pop()
        self.freqs[value] -= 1
        if not self.stacks_by_freq[self.highest_freq]:
            self.highest_freq -= 1
        return value
