from collections import Counter, deque
from heapq import heappop, heappush
from typing import List


def schedule_tasks(tasks: List[str], k: int) -> int:
    counts = Counter(tasks)
    maxheap = []
    for job, freq in counts.items():
        heappush(maxheap, (-freq, job))

    intervals = 0
    queue = deque()
    while maxheap:
        freq, job = heappop(maxheap)
        intervals += 1
        freq += 1  # freq is negative so adding 1 gets it closer to 0
        if freq != 0:
            queue.append((intervals, freq, job))
        while not maxheap and queue and intervals - queue[0][0] < k:
            intervals += 1
        while queue and intervals - queue[0][0] + 1 >= k:
            _, freq, job = queue.popleft()
            heappush(maxheap, (freq, job))
    return intervals


def main():
    print(
        "Minimum intervals needed to execute all tasks: "
        + str(schedule_tasks(["a", "a", "a", "b", "c", "c"], 2))
    )
    print(
        "Minimum intervals needed to execute all tasks: "
        + str(schedule_tasks(["a", "b", "a"], 3))
    )


main()
