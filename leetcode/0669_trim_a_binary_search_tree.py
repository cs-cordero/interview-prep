from utils import TreeNode


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        while root and root.val is not None:
            if root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left
            else:
                break

        if not root or root.val is None:
            return root

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
