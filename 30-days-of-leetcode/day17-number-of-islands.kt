class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        // Given a 2d grid map of '1's (land) and '0's (water), count the
        // number of islands. An island is surrounded by water and is formed by
        // connecting adjacent lands horizontally or vertically. You may assume
        // all four edges of the grid are all surrounded by water.
        val rowSize = grid.size
        val colSize = grid.firstOrNull()?.size ?: return 0

        val mutableGrid = grid.map {
            it.map {
                if (it == '1') true else false
            }.toMutableList()
        }

        fun markIsland(coordinate: Pair<Int, Int>) {
            val queue = mutableListOf(coordinate)
            while (queue.isNotEmpty()) {
                val (row, col) = queue.removeAt(0)
                listOf(
                    Pair(row - 1, col),
                    Pair(row, col + 1),
                    Pair(row + 1, col),
                    Pair(row, col - 1)
                ).filter {
                    it.first >= 0 &&
                    it.first < rowSize &&
                    it.second >= 0 &&
                    it.second < colSize &&
                    mutableGrid.getOrNull(it.first)?.getOrNull(it.second) ?: false
                }.forEach {
                    mutableGrid.getOrNull(it.first)?.set(it.second, false)
                    queue.add(it)
                }
            }
        }

        var result = 0
        mutableGrid.forEachIndexed { row, _row ->
            _row.forEachIndexed { col, value ->
                if (value == true) {
                    result += 1
                    markIsland(Pair(row, col))
                }
            }
        }
        return result
    }
}
