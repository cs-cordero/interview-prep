from heapq import heappop, heappush


class MedianOfAStream:
    def __init__(self) -> None:
        self.minheap = []
        self.maxheap = []

    def insert_num(self, num: int) -> None:
        heappush(self.minheap, num)
        while len(self.maxheap) < len(self.minheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def find_median(self) -> float:
        if not self.maxheap and not self.minheap:
            return 0.0

        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2

        return -self.maxheap[0]
