from utils import Empty, TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        if root.right and root.left:
            traverse_to_next(root.left).right = root.right
        if root.left:
            root.right = root.left
            root.left = None
        if root.right:
            self.flatten(root.right)


def traverse_to_next(root: TreeNode) -> None:
    while True:
        while root.right:
            root = root.right
        if root.left:
            root = root.left
        else:
            return root


root = TreeNode.from_array([1, 2, 5, 3, 4, Empty, 6])
expected = TreeNode(1)
current = expected
for i in range(2, 7):
    current.right = TreeNode(i)
    current = current.right

Solution().flatten(root)
assert TreeNode.subtrees_match(root, expected)
