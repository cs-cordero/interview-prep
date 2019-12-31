class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_alternate_k_elements(head: Node, k: int) -> Node:
    fake_head = Node(None)
    fake_head.next = head

    prev = fake_head
    curr = head
    while curr:
        prev.next = reverse_linked_list(curr, k)
        for _ in range(k + 1):
            prev = curr
            curr = curr.next
            if not curr:
                break
    return fake_head.next


def reverse_linked_list(head: Node, k: int) -> Node:
    assert k > 0

    fake_head = Node(None)
    fake_head.next = head

    prev = None
    curr = head
    while k > 0 and curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        k -= 1
    fake_head.next.next = curr
    return prev


head = Node(1)
current = head
for i in range(2, 9):
    current.next = Node(i)
    current = current.next

# head = reverse_linked_list(head, 2)
head = reverse_alternate_k_elements(head, 3)
head.print_list()
