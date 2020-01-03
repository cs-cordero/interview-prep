from collections import Counter, deque
from heapq import heappop, heappush


def reorganize_string(s: str, k: int) -> str:
    counts = Counter(s)
    maxheap = []
    for char, freq in counts.items():
        heappush(maxheap, (-freq, char))

    result = []
    queue = deque()
    while maxheap:
        freq, char = heappop(maxheap)
        result.append(char)
        freq += 1  # freq is negative so adding 1 gets it closer to 0
        if freq != 0:
            queue.append((len(result), freq, char))
        while queue and len(result) - queue[0][0] + 1 >= k:
            _, freq, char = queue.popleft()
            heappush(maxheap, (freq, char))
    return "" if queue else "".join(result)


def main():
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
