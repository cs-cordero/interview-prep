from typing import Optional


class ListNode:
    # Provided by LeetCode
    ...


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        next_pair = new_head.next

        new_head.next = head
        head.next = self.swapPairs(next_pair)
        return new_head
