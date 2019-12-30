from typing import Optional, Tuple


class Node:
    def __init__(self, value: int, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next


def is_palindromic_linked_list(head: Node) -> bool:
    midpoint, is_even = find_midpoint(head)
    end = reverse_linked_list(midpoint)
    tail = end
    start = head
    answer = True
    while start != midpoint:
        if start.value != end.value:
            answer = False
            break
        start = start.next
        end = end.next

    midpoint.next.next = None
    original_next = reverse_linked_list(tail)
    midpoint.next = original_next
    return answer


def find_midpoint(head: Node) -> Optional[Tuple[Node, bool]]:
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow, fast.next is not None


def reverse_linked_list(head: Node) -> Node:
    if not head.next:
        return head

    previous = head
    head = head.next
    temp = head.next
    while head:
        head.next = previous
        previous = head
        if temp is None:
            return head
        head = temp
        temp = head.next


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
