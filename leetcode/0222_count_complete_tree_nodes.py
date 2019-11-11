from typing import Optional


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
