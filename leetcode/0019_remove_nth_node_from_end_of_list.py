from typing import Optional


class ListNode:
    # Provided by Leetcode
    ...


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not n:
            return head

        fake_head = ListNode(None)
        fake_head.next = head

        def remove_helper(node: Optional[ListNode], k: int) -> int:
            if not node:
                return k

            count_from_end = remove_helper(node.next, k)
            if count_from_end == 0:
                node.next = node.next.next
            return count_from_end - 1

        remove_helper(fake_head, n)
        return fake_head.next
