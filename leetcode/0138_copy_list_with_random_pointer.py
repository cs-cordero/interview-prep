from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Optional


@dataclass(unsafe_hash=True)
class Node:
    val: Any
    next: Optional["Node"]
    random: Optional["Node"]


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        original_to_copy_map = {}

        def copy_helper(node: Optional[Node]) -> Optional[Node]:
            if not node:
                return None

            if node in original_to_copy_map:
                # Node already copied
                return original_to_copy_map[node]

            copied_node = Node(val=deepcopy(node.val), next=None, random=None)
            original_to_copy_map[node] = copied_node

            copied_node.next = copy_helper(node.next)
            copied_node.random = copy_helper(node.random)
            return copied_node

        return copy_helper(head)
