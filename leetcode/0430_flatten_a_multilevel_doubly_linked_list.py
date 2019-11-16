class Node:
    # Provided by Leetcode
    ...


class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return None

        if head.child:
            next_after_child_list = head.next  # 9

            flattened_child = self.flatten(head.child)
            head.next = flattened_child
            flattened_child.prev = head
            head.child = None

            if next_after_child_list:
                child = flattened_child
                while child and child.next:
                    child = child.next
                child.next = next_after_child_list
                next_after_child_list.prev = child

        next_node = self.flatten(head.next)
        if next_node:
            next_node.prev = head
        head.next = next_node
        return head
