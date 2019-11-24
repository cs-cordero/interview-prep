class Node:
    # Provided by Leetcode
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Node", insertVal: int) -> "Node":
        node = Node(val=insertVal)
        if head is None:
            node.next = node
            return node
        elif head.next == head:
            head.next = node
            node.next = head
            return head

        def should_insert(current: "Node") -> bool:
            is_end_of_list = current.val > current.next.val
            return (
                (
                    current.val <= node.val
                    and (is_end_of_list or node.val < current.next.val)
                )
                or (is_end_of_list and node.val < current.next.val)
                or current.next is head
            )

        current = head
        while not should_insert(current):
            current = current.next
        node.next = current.next
        current.next = node
        return head
