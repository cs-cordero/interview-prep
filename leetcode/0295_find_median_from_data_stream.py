from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.maxheap and num > -self.maxheap[0]:
            heappush(self.minheap, num)
        else:
            heappush(self.maxheap, -num)

        while len(self.maxheap) - len(self.minheap) > 1:
            heappush(self.minheap, -heappop(self.maxheap))

        while len(self.minheap) - len(self.maxheap) > 0:
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        if (len(self.maxheap) + len(self.minheap)) % 2 != 0:
            return float(-self.maxheap[0])
        return (-self.maxheap[0] + self.minheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
