/**
 * A binary matrix means that all elements are 0 or 1. For each individual row
 * of the matrix, this row is sorted in non-decreasing order.
 *
 * Given a row-sorted binary matrix binaryMatrix, return leftmost column
 * index(0-indexed) with at least a 1 in it. If such index doesn't exist, return
 * -1.
 * You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
 *
 *  BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y)
 *  (0-indexed).
 *  BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means
 *  the matrix is n * m.
 *
 *  Submissions making more than 1000 calls to BinaryMatrix.get will be judged
 *  Wrong Answer.  Also, any solutions that attempt to circumvent the judge will
 *  result in disqualification.
 *
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *     fun get(x:Int, y:Int):Int {}
 *     fun dimensions():List<Int> {}
 * }
 **/
class Solution {
    fun leftMostColumnWithOne(binaryMatrix: BinaryMatrix): Int {
        val dimensions = binaryMatrix.dimensions()
        val n = dimensions.elementAt(0)
        val m = dimensions.elementAt(1)

        var validRows = IntRange(0, n - 1).toSet()

        var leftColumn = 0
        var rightColumn = m - 1
        var result = -1
        while (leftColumn <= rightColumn) {
            val midColumn = (leftColumn + rightColumn) / 2
            val stillValidRows = validRows
                .filter { binaryMatrix.get(it, midColumn) == 1 }
                .toSet()

            if (stillValidRows.isEmpty()) {
                leftColumn = midColumn + 1
            } else {
                result = midColumn
                rightColumn = midColumn - 1
                validRows = validRows.intersect(stillValidRows)
            }
        }

        return result
    }
}
