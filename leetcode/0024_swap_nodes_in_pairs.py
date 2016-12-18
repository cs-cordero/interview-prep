from typing import Any, Optional


class ListNode:
    def __init__(self, x: Any) -> None:
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head = head.next

        if not new_head:
            return head

        current_node = head
        i = 0
        while current_node and current_node.next and current_node.next.next:
            if i % 2 != 0:
                temp = current_node.next
                current_node.next = current_node.next.next
                temp.next = current_node.next.next
                current_node.next.next = temp
            current_node = current_node.next
            i += 1

        if head.next:
            head.next = head.next.next
            new_head.next = head
        return new_head
