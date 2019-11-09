class TreeNode:
    # Provided by leetcode
    ...


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node: TreeNode):
            if node.left:
                left_valid, left_min, left_max = helper(node.left)
            else:
                left_valid = True
                left_min = left_max = None
            if node.right:
                right_valid, right_min, right_max = helper(node.right)
            else:
                right_valid = True
                right_min = right_max = None

            valid = (
                left_valid
                and right_valid
                and (left_max is None or node.val > left_max)
                and (right_min is None or node.val < right_min)
            )
            next_min = min(
                left_min if left_min else node.val,
                right_min if right_min else node.val,
                node.val,
            )
            next_max = max(
                left_max if left_max else node.val,
                right_max if right_max else node.val,
                node.val,
            )
            return valid, next_min, next_max

        return helper(root)[0] if root else True
