from typing import Optional


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        longest = float("-inf")

        def helper(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            nonlocal longest
            left = helper(node.left)
            right = helper(node.right)
            longest = max(longest, left + right + 1, max(left, right) + 1)
            return max(left, right) + 1

        helper(root)
        return longest - 1
