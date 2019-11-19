from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for source, target, cost in times:
            graph[source].append((target, cost))

        dist = [float("inf") for _ in range(N)]
        dist[K - 1] = 0
        priority_queue = [(0, K)]
        while priority_queue:
            expected_dist, node = heappop(priority_queue)
            if expected_dist > dist[node - 1]:
                continue

            for child, cost in graph[node]:
                next_dist = dist[node - 1] + cost
                if dist[child - 1] > next_dist:
                    dist[child - 1] = next_dist
                    heappush(priority_queue, (next_dist, child))

        result = max(dist)
        return result if result != float("inf") else -1
