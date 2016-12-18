from utils import TreeNode


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root or root.val is None:
            return 0

        if getattr(root, "max_seen", False):
            return root.max_seen

        # rob the root
        choice_1_value = root.val
        if root.left and root.left.left:
            choice_1_value += self.rob(root.left.left)
        if root.left and root.left.right:
            choice_1_value += self.rob(root.left.right)
        if root.right and root.right.left:
            choice_1_value += self.rob(root.right.left)
        if root.right and root.right.right:
            choice_1_value += self.rob(root.right.right)

        # don't rob the root
        choice_2_value = 0
        if root.left:
            choice_2_value += self.rob(root.left)
        if root.right:
            choice_2_value += self.rob(root.right)

        maximum = max(choice_1_value, choice_2_value)
        root.max_seen = maximum
        return root.max_seen


tree = TreeNode.from_array([3, 2, 3, TreeNode.EMPTY, 3, TreeNode.EMPTY, 1])
print(Solution().rob(tree))

tree2 = TreeNode.from_array([3, 4, 5, 1, 3, TreeNode.EMPTY, 1])
print(Solution().rob(tree2))
