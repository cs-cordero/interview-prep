from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Node:
    value: int
    parent: Optional["Node"] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    copies: int = 1
    count_less_than: int = 0


class BST:
    def __init__(self) -> None:
        self.root = None

    def push(self, value: int) -> int:
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return 0

        current = self.root
        result = 0
        while True:
            if current.value > value:  # move left
                current.count_less_than += 1
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif current.value < value:  # move right
                result += current.count_less_than + current.copies
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                current.copies += 1
                result += count_less_than
                break
        return result


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        bst = BST()
        for i, num in enumerate(reversed(nums)):
            result[len(nums) - i - 1] = bst.push(num)
        return result
