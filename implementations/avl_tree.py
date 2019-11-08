from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None
    height: int = 0

    def __repr__(self) -> str:
        left = f"Node({self.left.value})" if self.left else "None"
        right = f"Node({self.right.value})" if self.right else "None"
        return f"Node(value={self.value}, {left=}, {right=})"

    @property
    def left_height(self) -> int:
        return self.left.height if self.left else -1

    @property
    def right_height(self) -> int:
        return self.right.height if self.right else -1

    @property
    def balance_factor(self) -> int:
        return self.right_height - self.left_height

    @property
    def unbalanced(self) -> bool:
        return self.balance_factor not in (-1, 0, 1)

    def update(self) -> None:
        self.height = 1 + max(self.left_height, self.right_height)


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def _push(self, node: Optional[Node], value: int) -> Node:
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._push(node.left, value)
        elif value > node.value:
            node.right = self._push(node.right, value)

        node.update()
        return self.balance(node)

    def push(self, value: int) -> None:
        self.root = self._push(self.root, value)

    def balance(self, node: Node) -> Node:
        balance_factor = node.balance_factor
        if balance_factor >= 2:
            if node.right.balance_factor < 0:
                self.rotate_right(node.right)
            return self.rotate_left(node)
        elif balance_factor <= -2:
            if node.left.balance_factor > 0:
                self.rotate_left(node.lef)
            return self.rotate_right(node)
        return node

    def rotate_left(self, node: Node) -> Node:
        if not node.right:
            return None

        target = node.right
        node.right = target.left
        target.left = node
        node.update()
        target.update()

        if node == self.root:
            self.root = target
        return target

    def rotate_right(self, node: Node) -> Node:
        if not node.left:
            return None

        target = node.left
        node.left = target.right
        target.right = node
        node.update()
        target.update()

        if node == self.root:
            self.root = target
        return target


tree = AVLTree()
tree.push(3)
tree.push(10)
tree.push(0)
tree.push(8)
tree.push(12)
