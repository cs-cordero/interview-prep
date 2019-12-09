from collections import deque
from typing import List


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node is None:
                continue
            if len(result) == depth:
                result.append([])
            result[depth].append(node.val)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        for i in range(len(result)):
            if i % 2 == 0:
                continue
            result[i] = list(reversed(result[i]))
        return result
