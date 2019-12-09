from typing import Optional


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return not root or is_symmetric(root.left, root.right)


def is_symmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    if left is None and right is None:
        return True
    elif not (left is not None and right is not None):
        return False

    if left.val != right.val:
        return False
    return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)
