from bisect import insort
from collections import defaultdict, deque
from typing import Dict, List, Tuple


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(deque)
        ticket_count = defaultdict(int)
        for departure, arrival in tickets:
            insort(graph[departure], arrival)
            ticket_count[(departure, arrival)] += 1

        def helper(itinerary: List[str], remaining: Dict[Tuple[str, str], int]):
            current_airport = itinerary[-1]
            no_destinations = True
            for destination in graph[current_airport]:
                ticket = (current_airport, destination)
                if remaining.get(ticket) <= 0:
                    continue
                no_destinations = False
                next_remaining = remaining.copy()
                next_remaining[ticket] -= 1
                temp = helper(itinerary + [destination], next_remaining)
                if temp:
                    return temp

            if no_destinations and len(itinerary) - 1 == len(tickets):
                return itinerary

        return helper(["JFK"], ticket_count)


# print(
#     Solution().findItinerary(
#         [
#             ["EZE", "AXA"],
#             ["TIA", "ANU"],
#             ["ANU", "JFK"],
#             ["JFK", "ANU"],
#             ["ANU", "EZE"],
#             ["TIA", "ANU"],
#             ["AXA", "TIA"],
#             ["TIA", "JFK"],
#             ["ANU", "TIA"],
#             ["JFK", "TIA"],
#         ]
#     )
# )
print(
    Solution().findItinerary(
        [
            ["AXA", "EZE"],
            ["EZE", "AUA"],
            ["ADL", "JFK"],
            ["ADL", "TIA"],
            ["AUA", "AXA"],
            ["EZE", "TIA"],
            ["EZE", "TIA"],
            ["AXA", "EZE"],
            ["EZE", "ADL"],
            ["ANU", "EZE"],
            ["TIA", "EZE"],
            ["JFK", "ADL"],
            ["AUA", "JFK"],
            ["JFK", "EZE"],
            ["EZE", "ANU"],
            ["ADL", "AUA"],
            ["ANU", "AXA"],
            ["AXA", "ADL"],
            ["AUA", "JFK"],
            ["EZE", "ADL"],
            ["ANU", "TIA"],
            ["AUA", "JFK"],
            ["TIA", "JFK"],
            ["EZE", "AUA"],
            ["AXA", "EZE"],
            ["AUA", "ANU"],
            ["ADL", "AXA"],
            ["EZE", "ADL"],
            ["AUA", "ANU"],
            ["AXA", "EZE"],
            ["TIA", "AUA"],
            ["AXA", "EZE"],
            ["AUA", "SYD"],
            ["ADL", "JFK"],
            ["EZE", "AUA"],
            ["ADL", "ANU"],
            ["AUA", "TIA"],
            ["ADL", "EZE"],
            ["TIA", "JFK"],
            ["AXA", "ANU"],
            ["JFK", "AXA"],
            ["JFK", "ADL"],
            ["ADL", "EZE"],
            ["AXA", "TIA"],
            ["JFK", "AUA"],
            ["ADL", "EZE"],
            ["JFK", "ADL"],
            ["ADL", "AXA"],
            ["TIA", "AUA"],
            ["AXA", "JFK"],
            ["ADL", "AUA"],
            ["TIA", "JFK"],
            ["JFK", "ADL"],
            ["JFK", "ADL"],
            ["ANU", "AXA"],
            ["TIA", "AXA"],
            ["EZE", "JFK"],
            ["EZE", "AXA"],
            ["ADL", "TIA"],
            ["JFK", "AUA"],
            ["TIA", "EZE"],
            ["EZE", "ADL"],
            ["JFK", "ANU"],
            ["TIA", "AUA"],
            ["EZE", "ADL"],
            ["ADL", "JFK"],
            ["ANU", "AXA"],
            ["AUA", "AXA"],
            ["ANU", "EZE"],
            ["ADL", "AXA"],
            ["ANU", "AXA"],
            ["TIA", "ADL"],
            ["JFK", "ADL"],
            ["JFK", "TIA"],
            ["AUA", "ADL"],
            ["AUA", "TIA"],
            ["TIA", "JFK"],
            ["EZE", "JFK"],
            ["AUA", "ADL"],
            ["ADL", "AUA"],
            ["EZE", "ANU"],
            ["ADL", "ANU"],
            ["AUA", "AXA"],
            ["AXA", "TIA"],
            ["AXA", "TIA"],
            ["ADL", "AXA"],
            ["EZE", "AXA"],
            ["AXA", "JFK"],
            ["JFK", "AUA"],
            ["ANU", "ADL"],
            ["AXA", "TIA"],
            ["ANU", "AUA"],
            ["JFK", "EZE"],
            ["AXA", "ADL"],
            ["TIA", "EZE"],
            ["JFK", "AXA"],
            ["AXA", "ADL"],
            ["EZE", "AUA"],
            ["AXA", "ANU"],
            ["ADL", "EZE"],
            ["AUA", "EZE"],
        ]
    )
)
