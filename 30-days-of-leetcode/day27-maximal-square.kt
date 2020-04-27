class Solution {
    fun maximalSquare(matrix: Array<CharArray>): Int {
        var result = 0

        val N = matrix.size
        val M = matrix.getOrNull(0)?.size ?: return 0

        val dp = Array(N + 1) { IntArray(M + 1) }
        for (i in 1..N) {
            for (j in 1..M) {
                if (matrix[i - 1][j - 1] == '1') {
                    dp[i][j] = minOf(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    result = maxOf(result, dp[i][j] * dp[i][j])
                }
            }
        }
        return result
    }
}
