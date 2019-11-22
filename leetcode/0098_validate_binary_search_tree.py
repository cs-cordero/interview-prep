from typing import Optional


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(
            node: Optional[TreeNode], lower=float("-inf"), upper=float("inf")
        ) -> bool:
            if node is None:
                return True

            left = helper(node.left, lower=lower, upper=node.val)
            right = helper(node.right, lower=node.val, upper=upper)
            return left and right and lower < node.val and node.val < upper

        return helper(root)
