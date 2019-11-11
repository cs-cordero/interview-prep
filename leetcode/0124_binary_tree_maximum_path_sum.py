from typing import Optional


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return float("-inf")

        best = float("-inf")

        def helper(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return float("-inf")

            left = helper(node.left)
            right = helper(node.right)
            best = max(
                best,
                left + node.val + right,
                left + node.val,
                node.val + right,
                left,
                right,
                node.val,
            )
            return max(left + node.val, right + node.val, node.val)

        helper(root)
        return best
