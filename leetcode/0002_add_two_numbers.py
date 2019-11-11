from typing import Optional


class ListNode:
    # Provided by Leetcode
    ...


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add_helper(
            node1: Optional[ListNode], node2: Optional[ListNode], remainder: int
        ) -> ListNode:
            if not node1 and not node2 and not remainder:
                return None

            added = (
                (node1.val if node1 else 0) + (node2.val if node2 else 0) + remainder
            )
            digit = added % 10
            remainder = added // 10

            node = ListNode(digit)
            node.next = add_helper(
                node1.next if node1 else None, node2.next if node2 else None, remainder
            )
            return node

        return add_helper(l1, l2, 0)
