from typing import Optional, Tuple


class Node:
    # Provided by Leetcode
    ...


class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
        def helper(node: Optional[Node]) -> Tuple[Optional[Node], Optional[Node]]:
            if node is None:
                return None, None

            left_head, left_tail = helper(node.left)
            right_head, right_tail = helper(node.right)
            if left_tail:
                left_tail.right = node
            if right_head:
                right_head.left = node
            node.left = left_tail
            node.right = right_head
            return left_head or node, right_tail or node

        if root is None:
            return None

        head, tail = helper(root)
        head.left = tail
        tail.right = head
        return head
