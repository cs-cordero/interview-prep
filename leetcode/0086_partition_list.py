class ListNode:
    # Provided by Leetcode
    ...


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        fake_head = ListNode(None)
        fake_head.next = head

        partition = fake_head
        current = fake_head
        while current and current.next:
            if current.next.val < x:
                temp = current.next
                current.next = current.next.next
                temp.next = partition.next
                partition.next = temp
                if current == partition:
                    current = current.next
                partition = partition.next
            else:
                current = current.next
        return fake_head.next
