class Solution {
    fun diameterOfBinaryTree(root: TreeNode?): Int {
        //  Given a binary tree, you need to compute the length of the diameter
        //  of the tree. The diameter of a binary tree is the length of the
        //  longest path between any two nodes in a tree. This path may or may
        //  not pass through the root.
        var diameter = 0

        fun getHeight(node: TreeNode?): Int {
            if (node == null) return 0

            val heightLeft = getHeight(node.left)
            val heightRight = getHeight(node.right)
            val lengthDiameter = heightLeft + heightRight

            diameter = if (lengthDiameter > diameter) lengthDiameter else diameter
            return 1 + if (heightLeft > heightRight) heightLeft else heightRight
        }

        getHeight(root)
        return diameter
    }
}
