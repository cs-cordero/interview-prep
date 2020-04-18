class Solution {
    fun minPathSum(grid: Array<IntArray>): Int {
        // Given a m x n grid filled with non-negative numbers, find a path
        // from top left to bottom right which minimizes the sum of all numbers
        // along its path.
        //
        // Note: You can only move either down or right at any point in time.
        for (row in grid.indices) {
            for (col in grid[row].indices) {
                if (row == 0 && col == 0) continue
                val fromUp = if (row - 1 >= 0) grid[row - 1][col] else Int.MAX_VALUE
                val fromLeft = if (col - 1 >= 0) grid[row][col - 1] else Int.MAX_VALUE
                grid[row][col] += Math.min(fromUp, fromLeft)
            }
        }
        return grid.last().last()
    }
}
