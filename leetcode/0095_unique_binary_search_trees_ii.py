from typing import List


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(lower: int, upper: int) -> List[TreeNode]:
            result = []
            for root_val in range(lower, upper):
                left_roots = helper(lower, root_val)
                right_roots = helper(root_val + 1, upper)
                for left in left_roots:
                    for right in right_roots:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        result.append(root)

            if not result:
                return [None]
            return result

        if n < 1:
            return []
        return helper(1, n + 1)
