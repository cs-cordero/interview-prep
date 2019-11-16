from typing import List, Optional


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        deleted = set(to_delete)
        deleted.add(0)
        fake_root = TreeNode(0)
        fake_root.left = root

        result = []

        def helper(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None

            node.left = helper(node.left)
            node.right = helper(node.right)

            is_deleted = node.val in deleted
            if is_deleted:
                for child in (node.left, node.right):
                    if child and child.val not in deleted:
                        result.append(child)
                return None
            return node

        helper(fake_root)
        return result
