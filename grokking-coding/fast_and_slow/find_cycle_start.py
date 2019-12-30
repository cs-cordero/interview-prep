from typing import Optional


class Node:
    ...


def find_cycle_start(head: Node) -> Optional[Node]:
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if fast != slow:
        return None
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast
