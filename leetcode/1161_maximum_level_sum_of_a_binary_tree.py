from collections import defaultdict
from typing import Optional


class TreeNode:
    # Provided by Leetcode
    pass


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth_sums = defaultdict(int)

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return None
            depth_sums[depth] += node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        best_depth = 0
        highest_sum = float("-inf")
        for depth in sorted(depth_sums):
            if depth_sums[depth] > highest_sum:
                highest_sum = depth_sums[depth]
                best_depth = depth
        return best_depth
