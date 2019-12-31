class Node:
    def __init__(self, value: int, next=None) -> None:
        self.value = value
        self.next = next

    def print_list(self) -> None:
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def rotate(head: Node, rotations: int) -> Node:
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = head

    prev = tail
    current = head
    for _ in range(rotations):
        prev = prev.next
        current = current.next
    prev.next = None
    return current
