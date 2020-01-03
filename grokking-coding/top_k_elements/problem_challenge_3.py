from collections import defaultdict
from heapq import heappop, heappush


class FrequencyStack:
    def __init__(self) -> None:
        self.heap = []
        self.freq = defaultdict(int)
        self.id = 0

    def push(self, num: int) -> None:
        self.freq[num] += 1
        key = (-self.freq[num], -self.id, num)
        self.id += 1
        heappush(self.heap, key)

    def pop(self) -> int:
        _, _, num = heappop(self.heap)
        self.freq[num] -= 1
        return num


def main():
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())


main()
