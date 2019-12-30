from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next


def reorder(head: Node) -> Node:
    midpoint = get_midpoint(head)
    end = reverse_linked_list(midpoint)
    begin = head

    while begin is not None and end is not None:
        temp = end.next
        if begin.next != end:
            end.next = begin.next
        begin.next = end
        end = temp
        begin = begin.next.next
    return head


def get_midpoint(head: Node) -> Node:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse_linked_list(head: Node) -> Node:
    prev = None
    while head is not None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev
