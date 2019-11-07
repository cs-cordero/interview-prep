from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass
class Node:
    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None


@dataclass
class BinarySearchTree:
    root: Optional[Node] = None

    def traverse_preorder(self) -> Iterable[Node]:
        def preorder_helper(node: Optional[Node]) -> Iterable[Node]:
            if not node:
                return None
            yield node
            yield from preorder_helper(node.left)
            yield from preorder_helper(node.right)

        if self.root is None:
            return None
        yield from preorder_helper(self.root)

    def traverse_inorder(self) -> Iterable[Node]:
        def inorder_helper(node: Optional[Node]) -> Iterable[Node]:
            if not node:
                return None
            yield from inorder_helper(node.left)
            yield node
            yield from inorder_helper(node.right)

        if self.root is None:
            return None
        yield from inorder_helper(self.root)

    def traverse_postorder(self) -> Iterable[Node]:
        def postorder_helper(node: Optional[Node]) -> Iterable[Node]:
            if not node:
                return None
            yield from postorder_helper(node.left)
            yield from postorder_helper(node.right)
            yield node

        if self.root is None:
            return None
        yield from postorder_helper(self.root)

    def insert(self, node: Node) -> None:
        if self.root is None:
            self.root = node
            return None

        current = self.root
        while True:
            if current.value < node.value:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
            elif current.value > node.value:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                break
        return None

    def remove(self, value: int) -> None:
        def removal_helper(root: Optional[Node], value: int) -> Optional[Node]:
            if root is None:
                return None

            if root.value < value:
                # the node to remove is towards the left
                root.right = removal_helper(root.right, value)
            elif root.value > value:
                # the node to remove is towards the left
                root.left = removal_helper(root.left, value)
            else:
                # root is the node to remove
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    target = root.left
                    while target.right:
                        target = target.right
                    root.value = target.value
                    root.left = removal_helper(root.left, target.value)
            return root

        removal_helper(self.root, value)


bst = BinarySearchTree()
bst.insert(Node(7))
bst.insert(Node(20))
bst.insert(Node(5))
bst.insert(Node(15))
bst.insert(Node(10))
bst.insert(Node(4))
bst.insert(Node(4))
bst.insert(Node(33))
bst.insert(Node(2))
bst.insert(Node(25))
bst.insert(Node(6))
assert bst.root.value == 7
assert bst.root.left.value == 5
assert bst.root.left.left.value == 4
assert bst.root.left.left.left.value == 2
assert bst.root.left.left.right is None
assert bst.root.left.right.value == 6
assert bst.root.left.right.left is None
assert bst.root.left.right.right is None
assert bst.root.right.value == 20
assert bst.root.right.left.value == 15
assert bst.root.right.left.left.value == 10
assert bst.root.right.left.right is None
assert bst.root.right.right.value == 33
assert bst.root.right.right.left.value == 25
assert bst.root.right.right.right is None


bst2 = BinarySearchTree()
bst2.insert(Node(0))
bst2.insert(Node(-2))
bst2.insert(Node(2))
bst2.insert(Node(-4))
bst2.insert(Node(-1))
bst2.insert(Node(3))
bst2.remove(0)
assert bst2.root.value == -1
assert bst2.root.left.value == -2

bst3 = BinarySearchTree()
bst3.insert(Node(11))
bst3.insert(Node(6))
bst3.insert(Node(15))
bst3.insert(Node(3))
bst3.insert(Node(8))
bst3.insert(Node(13))
bst3.insert(Node(17))
bst3.insert(Node(1))
bst3.insert(Node(5))
bst3.insert(Node(12))
bst3.insert(Node(14))
bst3.insert(Node(19))

preorder = [node.value for node in bst3.traverse_preorder()]
inorder = [node.value for node in bst3.traverse_inorder()]
postorder = [node.value for node in bst3.traverse_postorder()]

assert preorder == [11, 6, 3, 1, 5, 8, 15, 13, 12, 14, 17, 19]
assert inorder == [1, 3, 5, 6, 8, 11, 12, 13, 14, 15, 17, 19]
assert postorder == [1, 5, 3, 8, 6, 12, 14, 13, 19, 17, 15, 11]
