class ListNode:
    # Provided by Leetcode
    ...


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        fake_head = ListNode(None)
        fake_head.next = head
        head = fake_head

        while head:
            local_head = reverse_up_to_k(head.next, k - 1)
            if local_head is None:
                break
            head.next = local_head
            for _ in range(k):
                head = head.next
                if head is None:
                    break
        return fake_head.next


def reverse_up_to_k(node: ListNode, k: int) -> None:
    if node is None:
        return None
    if k == 0:
        return node
    new_head = reverse_up_to_k(node.next, k - 1)
    if new_head is None:
        return None
    temp = node.next.next
    node.next.next = node
    node.next = temp
    return new_head
