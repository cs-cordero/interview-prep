from collections import deque


class TreeNode:
    # Provided by Leetcode
    ...


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        opponent_node = find_node(root, x)
        left_count = count_tree(opponent_node.left)
        right_count = count_tree(opponent_node.right)
        parent_count = n - left_count - right_count - 1
        return (
            (left_count > right_count + parent_count)
            or (right_count > left_count + parent_count)
            or (parent_count > left_count + right_count)
        )


def find_node(root: TreeNode, target: int) -> TreeNode:
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node:
            continue
        if node.val == target:
            return node
        queue.append(node.left)
        queue.append(node.right)

    assert False, "Node doesn't exist"


def count_tree(root: TreeNode) -> int:
    if not root:
        return 0
    queue = deque([root])
    result = 0
    while queue:
        node = queue.popleft()
        result += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
