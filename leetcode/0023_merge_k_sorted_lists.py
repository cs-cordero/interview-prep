import heapq
from typing import List


class ListNode:
    # Provided by Leetcode
    ...


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(head.val, i) for i, head in enumerate(lists) if head]
        heapq.heapify(heap)

        fake_head = ListNode(None)
        current = fake_head
        while heap:
            _, list_i = heapq.heappop(heap)
            node = lists[list_i]
            current.next = node
            current = node
            lists[list_i] = node.next
            if node.next:
                heapq.heappush(heap, (node.next.val, list_i))
        return fake_head.next
