class Solution {
    fun bstFromPreorder(preorder: IntArray): TreeNode? {
        // Return the root node of a binary search tree that matches the given preorder traversal.
        //
        // (Recall that a binary search tree is a binary tree where for every
        // node, any descendant of node.left has a value < node.val, and any
        // descendant of node.right has a value > node.val.  Also recall that a
        // preorder traversal displays the value of the node first, then
        // traverses node.left, then traverses node.right.)
        //
        // Definition for a binary tree node.
        // class TreeNode(var `val`: Int) {
        //     var left: TreeNode? = null
        //     var right: TreeNode? = null
        // }
        var root: TreeNode? = null

        val monotonicNodeStack = mutableListOf<TreeNode>()
        preorder.forEach {
            val newNode = TreeNode(it)
            if (monotonicNodeStack.isEmpty()) {
                root = newNode
            } else {
                var parentNode = monotonicNodeStack.last()
                if (newNode.`val` < parentNode.`val`) {
                    parentNode.left = newNode
                } else {
                    while (
                        monotonicNodeStack.isNotEmpty() &&
                        newNode.`val` >= monotonicNodeStack.last().`val`
                    ) {
                        parentNode = monotonicNodeStack.removeAt(monotonicNodeStack.lastIndex)
                    }
                    parentNode.right = newNode
                }
            }
            monotonicNodeStack.add(newNode)
        }

        return root
    }
}
