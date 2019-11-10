from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    value: int
    index: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def _push(self, node: Node, value: int, index: int) -> Node:
        if not node:
            return Node(value, index)

        if value == node.value:
            node.index = min(node.index, index)
        elif value < node.value:
            node.left = self._push(node.left, value, index)
        else:
            node.right = self._push(node.right, value, index)
        return node

    def push(self, value: int, index: int) -> None:
        self.root = self._push(self.root, value, index)

    def search_lowest_above_value(self, value: int) -> Optional[int]:
        node = self.root
        best = None
        while node:
            if value == node.value:
                return node.index
            elif value <= node.value:
                best = node
                node = node.left
            else:
                node = node.right
        return best.index if best else None

    def search_highest_below_value(self, value: int) -> Optional[int]:
        node = self.root
        best = None
        while node:
            if value == node.value:
                return node.index
            elif value >= node.value:
                best = node
                node = node.right
            else:
                node = node.left
        return best.index if best else None


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        dp = [[False for _ in range(len(A))] for _ in range(2)]
        dp[0][-1] = True
        dp[1][-1] = True

        bst = BinarySearchTree()
        bst.push(A[-1], len(A) - 1)

        answer = 1
        for i in range(len(A) - 2, -1, -1):
            current_value = A[i]
            lowest_above_value = bst.search_lowest_above_value(current_value)
            highest_below_value = bst.search_highest_below_value(current_value)

            if lowest_above_value:
                dp[0][i] = dp[1][lowest_above_value]
            if highest_below_value:
                dp[1][i] = dp[0][highest_below_value]
            if dp[0][i] is True:
                answer += 1
            bst.push(current_value, i)
        return answer
