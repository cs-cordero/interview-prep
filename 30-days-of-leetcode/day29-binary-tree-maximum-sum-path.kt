fun maxPathSum(root: TreeNode?): Int {
    var result = root?.let { it.`val` } ?: return 0

    fun maxPathSumHelper(node: TreeNode?): Int {
        if (node == null) {
            return 0
        } else {
            val fromLeft = maxPathSumHelper(node.left)
            val fromRight = maxPathSumHelper(node.right)

            val through = maxOf(
                maxOf(fromLeft, fromRight) + node.`val`,
                node.`val`
            )
            val across = fromLeft + fromRight + node.`val`

            result = maxOf(result, across, through)
            return through
        }
    }

    maxPathSumHelper(root)
    return result
}
