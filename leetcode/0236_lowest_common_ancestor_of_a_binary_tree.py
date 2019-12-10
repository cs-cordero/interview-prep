class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        parent_map = {root: None}

        def build_parent_map(node: TreeNode) -> None:
            if node.left:
                parent_map[node.left] = node
                build_parent_map(node.left)
            if node.right:
                parent_map[node.right] = node
                build_parent_map(node.right)

        def get_depth(node: TreeNode) -> int:
            depth = 0
            while node:
                depth += 1
                node = parent_map[node]
            return depth

        build_parent_map(root)
        p_depth = get_depth(p)
        q_depth = get_depth(q)
        while p_depth > q_depth:
            p = parent_map[p]
            p_depth -= 1

        while q_depth > p_depth:
            q = parent_map[q]
            q_depth -= 1

        while p != q:
            p = parent_map[p]
            q = parent_map[q]
        return p
