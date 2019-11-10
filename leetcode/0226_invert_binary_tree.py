class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
