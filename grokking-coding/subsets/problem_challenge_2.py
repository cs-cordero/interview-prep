from typing import List


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n: int):
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

    return helper(1, n + 1)


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()
