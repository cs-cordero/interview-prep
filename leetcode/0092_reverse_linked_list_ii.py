from typing import Optional


class ListNode:
    # Provided by Leetcode
    ...


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def helper(
            node: ListNode, start: Optional[ListNode], a: int, b: int
        ) -> ListNode:
            reverse_head = node if a == 0 else start

            if b == 0:
                start.next = node.next
                return node

            tail = helper(node.next, reverse_head, a - 1, b - 1)
            if a <= 0:
                node.next.next = node
                return tail

            node.next = tail
            return node

        return helper(head, None, m - 1, n - 1)
