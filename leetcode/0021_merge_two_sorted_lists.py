class ListNode:
    # Provided by Leetcode
    ...


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake_head = ListNode(None)
        current = fake_head
        while l1 or l2:
            if l2 is None or (l1 and l1.val <= l2.val):
                next_node = l1
                l1 = l1.next
            else:
                next_node = l2
                l2 = l2.next

            current.next = next_node
            current = current.next
        return fake_head.next
