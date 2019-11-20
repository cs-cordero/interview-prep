from typing import List


class TreeNode:
    # Provided by Leetcode:
    ...


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None

        root = TreeNode(pre[0])

        if len(pre) == 1:
            return root

        # count of nodes left of pre[1]
        partition = post.index(pre[1])

        root.left = self.constructFromPrePost(pre[1 : partition + 2], post[:partition])
        root.right = self.constructFromPrePost(
            pre[partition + 2 :], post[partition + 1 : -1]
        )
        return root
